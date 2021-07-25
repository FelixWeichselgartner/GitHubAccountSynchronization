# GitHub Account Synchronization

Automatically synchronize all your repositories (and all starred repositories) on your local drive. If the repository already exists it will be pulled to the newest commit, otherwise it will be cloned.

## Usage:
* Create a GitHub-API-Token: https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token
* Save this token in a file called `api_token.py` with the variable name `mytoken = '<YOUR TOKEN HERE>'`
* Install requirements: `pip install -r requirements.txt`
* If you do not want to synchronize starred repositories you can uncomment this is `main.py`
* To update and clone repositories execute `main.py`
