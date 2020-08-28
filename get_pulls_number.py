import requests
import json


def get_pull_numbers(GITHUB_URL, GITHUB_TOKEN, state="all"):
    GITHUB_URL += "pulls?state="+state
    response = requests.get(GITHUB_URL, auth=('', GITHUB_TOKEN))
    lists = json.loads(response.text)
    numbers = []
    for dic in lists:
        numbers.append(int(dic["number"]))
    return numbers


def get_change_files(GITHUB_URL, GITHUB_TOKEN, number, include_file=None):
    URL = GITHUB_URL + "pulls/" + str(number) + "/files"
    response = requests.get(URL, auth=('', GITHUB_TOKEN))
    lists = json.loads(response.text)
    result = {}
    filenames = [dic["filename"] for dic in lists]
    if include_file is not None and include_file not in filenames:
        return {}
    for dic in lists:
        result[dic["filename"]] = {
            "additions": int(dic["additions"]),
            "deletions": int(dic["deletions"]),
            "changes": int(dic["changes"])
            }
    return result


def concerened_files(GITHUB_URL, GITHUB_TOKEN, concerened_file=None):
    pull_numbers = get_pull_numbers(GITHUB_URL, GITHUB_TOKEN)
    res = {}
    for i, pull_number in enumerate(pull_numbers):
        print(i, "/", len(pull_numbers))
        change_hash = get_change_files(GITHUB_URL, GITHUB_TOKEN, pull_number, include_file=concerened_file)
        for filename, value in change_hash.items():
            if filename not in res:
                res[filename] = value
            else:
                for k, v in value.items():
                    res[filename][k] += v
    return res


if __name__ == "__main__":
    GITHUB_TOKEN = '133aa0492317ea650c89a4ba9dcd135fc393e46e'
    GITHUB_URL = "https://api.github.com/repos/oky-123/soc_information_api/"
    res = concerened_files(GITHUB_URL, GITHUB_TOKEN, concerened_file="app/models/student.rb")
    tmp = []
    for k, v in res.items():
        tmp.append([v["changes"], k])
    tmp = sorted(tmp)
    for changed, filename in tmp:
        print(filename, changed)
