from os import environ
import sys
import requests

PROJECT_ID = environ.get('PROJECT_ID')
ACCESS_TOKEN = environ.get('ACCESS_TOKEN')
BRANCH = environ.get('BRANCH')

if (PROJECT_ID is None) or (ACCESS_TOKEN is None) or (BRANCH is None):
    print("Missing environment variables. See https://github.com/hatamiarash7/Gitlab-CommitCounter for help.")
    sys.exit(0)

url = "https://gitlab.com/api/v4/projects/" + \
    PROJECT_ID + "/repository/commits?ref_name=" + BRANCH

response = requests.head(url, headers={
    "PRIVATE-TOKEN": ACCESS_TOKEN})

try:
    print(response.headers["x-total"])
except:
    print("Something is wrong !!")
    print("Check environment variables. See https://github.com/hatamiarash7/Gitlab-CommitCounter for help.")
