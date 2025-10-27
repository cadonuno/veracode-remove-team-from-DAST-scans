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

## Installation
Clone this repository:
    git clone https://github.com/cadonuno/veracode-start-scan.git

Install dependencies:

    cd /veracode-start-scan
    pip install -r requirements.txt

## Run
    python ./src/veracode-remove-team-from-dast.py (arguments)

## Supported Arguments:

- `-vid`, `--veracode_api_key_id` - Veracode API key ID to use - a non-human/API account is recommended.
- `-vkey`, `--veracode_api_key_secret` - Veracode API key secret to use - a non-human/API account is recommended.
- `-t`, `--team` - Name of the team to remove from DAST scans.
