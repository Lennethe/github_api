import requests
import json
import USER


def url_to_json(GITHUB_URL, GITHUB_TOKEN):
    response = requests.get(GITHUB_URL, auth=('', GITHUB_TOKEN))
    return json.loads(response.text)


def get_pull_numbers(GITHUB_URL, GITHUB_TOKEN, state="all"):
    GITHUB_URL += "pulls?state="+state
    response = url_to_json(GITHUB_URL, GITHUB_TOKEN)
    numbers = []
    for dic in response:
        numbers.append(int(dic["number"]))
    return numbers


def get_change_hash(GITHUB_URL, GITHUB_TOKEN, number, include_file=None):
    GITHUB_URL += "pulls/" + str(number) + "/files"
    pull_request = url_to_json(GITHUB_URL, GITHUB_TOKEN)
    filenames = [each_file["filename"] for each_file in pull_request]
    if include_file is not None and include_file not in filenames:
        return {}
    result = {}
    for each_file in pull_request:
        result[each_file["filename"]] = {
            "additions": int(each_file["additions"]),
            "deletions": int(each_file["deletions"]),
            "changes": int(each_file["changes"])
            }
    return result


def concerened_files(GITHUB_URL, GITHUB_TOKEN, concerened_file=None):
    pull_numbers = get_pull_numbers(GITHUB_URL, GITHUB_TOKEN)
    res = {}
    for i, pull_number in enumerate(pull_numbers):
        print(i, "/", len(pull_numbers))
        change_hash = get_change_hash(GITHUB_URL, GITHUB_TOKEN, pull_number, include_file=concerened_file)
        for filename, value in change_hash.items():
            if filename not in res:
                res[filename] = value
            else:
                for k, v in value.items():
                    res[filename][k] += v
    return res


if __name__ == "__main__":
    GITHUB_TOKEN = USER.GITHUB_TOKEN
    GITHUB_URL = USER.GITHUB_URL
    concerened_file = USER.CONCERNED_FILE
    res = concerened_files(GITHUB_URL, GITHUB_TOKEN, concerened_file=concerened_file)
    tmp = []
    for k, v in res.items():
        tmp.append([v["changes"], k])
    tmp = sorted(tmp)
    for changed, filename in tmp:
        print(filename, changed)
