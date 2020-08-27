import requests
import json

GITHUB_TOKEN = 'f461f35be967a3ec50ae2b73704a605192751d64'
GITHUB_BASEURL = 'https://api.github.com/repos/oky-123/soc_information_api/issues'

response = requests.get(GITHUB_BASEURL, auth=('', GITHUB_TOKEN))

lists = json.loads(response.text)

print(lists)
