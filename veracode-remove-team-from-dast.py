import argparse
import sys
import json
import time
from veracode_api_py import Teams, Analyses, apihelper

def get_team_id(team_to_find):
    matches = Teams().get_by_name(team_to_find)
    if len(matches) == 0:
        return None

    for match in matches:
        if team_to_find == match["team_name"].strip():
            return match["team_legacy_id"]

    return None

def remove_team(new_teams_list, dast_scan, attempt):
    print(f"Removing team from scan: {dast_scan["name"]}")
    print(f"New teams list: {new_teams_list}")
    dast_scan["visibility"]["team_identifiers"] = new_teams_list
    if len(new_teams_list) == 0:
        dast_scan["visibility"]["setup_type"] = "SEC_LEADS_ONLY"
    request_uri = Analyses().base_url + '/{}'.format(dast_scan["analysis_id"])

    try:
        apihelper.APIHelper()._rest_request(request_uri,"PUT",params={},body=json.dumps(dast_scan))
        return True, True
    except Exception as e:
        if attempt < 10:
            wait_time=attempt*10
            print(f"Failed to update scan '{dast_scan["name"]}', waiting {wait_time} seconds")
            time.sleep(wait_time)
            return False, True
    return False, False

def remove_team_from_dast_if_present(team_id, dast_scan):
    new_teams_list=[]
    found_team_to_remove=False
    if "visibility" in dast_scan and "team_identifiers" in dast_scan["visibility"]:
        for team in dast_scan["visibility"]["team_identifiers"]:
            if str(team_id) == team:
                found_team_to_remove = True
            else:
                new_teams_list.append(team)
            
    if found_team_to_remove:
        attempt = 0
        should_retry = True
        while should_retry:
            attempt+=1
            has_succeded, should_retry = remove_team(new_teams_list, dast_scan, attempt)
            if has_succeded:
                return None
            if not should_retry:
                return dast_scan["name"]

def main():
    parser = argparse.ArgumentParser(
        description="This script starts a scan in Veracode."
    )

    parser.add_argument(
        "-t",
        "--team",
        help="Name of the team to remove from DAST scans.",
        required=True
    )

    args = parser.parse_args()

    team_to_remove = args.team.strip()
    print(f"Looking for team named {team_to_remove}")
    team_id = get_team_id(team_to_remove)
    if not team_id:
        print(f"Team named {team_to_remove} not found")
        sys.exit(-1)

    print("Fetching list of DAST scans")
    all_dast_scans = Analyses().get_all()

    print(f"Found {len(all_dast_scans)} DAST scans")
    errors = []
    for dast_scan in all_dast_scans:
        full_analysis = Analyses().get(dast_scan["analysis_id"])
        error = remove_team_from_dast_if_present(team_id, full_analysis)
        if error:
            errors.append(error)

    print("----------------------------")
    print("Finished updating DAST scans")
    if errors:
        print("Failed to update the following DAST scans:")
        for error in errors:
            print(f" - {error}")

if __name__ == '__main__':
    main()