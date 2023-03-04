""" Count commits for gitlab project """
from os import environ
import sys
import requests

# Get the required environment variables
PROJECT_ID = environ.get('PROJECT_ID')
ACCESS_TOKEN = environ.get('ACCESS_TOKEN')
BRANCH = environ.get('BRANCH')

# Check if any of the environment variables are missing and exit if so
if (PROJECT_ID is None) or (ACCESS_TOKEN is None) or (BRANCH is None):
    print("Missing variables. Check https://github.com/hatamiarash7/Gitlab-CommitCounter.")
    sys.exit(0)

# Construct the API URL using the environment variables
url = f"https://gitlab.com/api/v4/projects/{PROJECT_ID}/repository/commits?ref_name={BRANCH}"

# Send a HEAD request to the API with the authentication token
response = requests.head(url, headers={
    "PRIVATE-TOKEN": ACCESS_TOKEN})

try:
    # Try to get the value of the x-total header from the response
    x_total = response.headers.get("x-total")
    if x_total is not None:
        # If the value is not None, print it
        print(x_total)
    else:
        # If the value is None, something went wrong
        print("Something is wrong !!")
        print("Check variables. See https://github.com/hatamiarash7/Gitlab-CommitCounter.")
except Exception as e:  # pylint: disable=broad-except
    # Catch any exceptions and print an error message with the exception details
    print("Something is wrong !!")
    print("Check variables. See https://github.com/hatamiarash7/Gitlab-CommitCounter.")
    print(f"Exception: {str(e)}")
