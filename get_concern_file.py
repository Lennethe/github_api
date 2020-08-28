import requests
import json


def get_url(rest_url):
    GITHUB_TOKEN = '133aa0492317ea650c89a4ba9dcd135fc393e46e'
    GITHUB_URL = 'https://api.github.com/repos/Lennethe/github_api/'
#    GITHUB_URL = "https://api.github.com/repos/oky-123/soc_information_api/"
    GITHUB_URL += rest_url
    response = requests.get(GITHUB_URL, auth=('', GITHUB_TOKEN))
    lists = json.loads(response.text)
    return lists


GITHUB_TOKEN = '133aa0492317ea650c89a4ba9dcd135fc393e46e'
GIT_URL = "https://api.github.com/repos/oky-123/soc_information_api/"


def get_change_files(base_url, number, TOKEN):
    URL = base_url + "pulls/" + str(number) + "/files"
    response = requests.get(URL, auth=('', TOKEN))
    lists = json.loads(response.text)
    return lists


def res_to_file_dic(response):
    result = {}
    for dic in response:
        result[dic["filename"]] = {
            "additions": int(dic["additions"]),
            "deletions": int(dic["deletions"]),
            "changes": int(dic["changes"])
            }
    return result


print(res_to_file_dic(get_change_files(GIT_URL, 2, GITHUB_TOKEN)))
