# Veracode scan workflow plugin
Updates all DAST scans for your organization, removing a specific team from them.

## Requirements:
- Python 3.12+

## Required Veracode Roles and Permissions:
> ___Note___ - all roles can be replaced by an equivalent Custom Role (if available)
- One of the following roles:
  - Administrator
  - Creator
    - Additional access to Dynamic Scans is required
  - Submitter
    - Additional access to Dynamic Scans is required

## Setup

Clone this repository:

    git clone https://github.com/cadonuno/veracode-remove-team-from-DAST-scans

Install dependencies:

    cd veracode-remove-team-from-DAST-scans
    pip install -r requirements.txt

(Optional) Save Veracode API credentials in `~/.veracode/credentials`

    [default]
    veracode_api_key_id = <YOUR_API_KEY_ID>
    veracode_api_key_secret = <YOUR_API_KEY_SECRET>


## Run
If you have saved credentials as above you can run:

    python veracode-remove-team-from-dast.py (arguments)

Otherwise you will need to set environment variables:

    export VERACODE_API_KEY_ID=<YOUR_API_KEY_ID>
    export VERACODE_API_KEY_SECRET=<YOUR_API_KEY_SECRET>
    python veracode-remove-team-from-dast.py (arguments)

## Supported Arguments:
- `-t`, `--team` - Name of the team to remove from DAST scans.
