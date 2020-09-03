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


def get_reviewers(GITHUB_URL, GITHUB_TOKEN, number, concerened_file=None):
    GITHUB_URL += "pulls/" + str(number) + "/comments"
    response = requests.get(GITHUB_URL, auth=('', GITHUB_TOKEN))
    review_infos = json.loads(response.text)
    result = []
    for review_info in review_infos:
        if concerened_file is not None and concerened_file != review_info["path"]:
            continue
        result.append(review_info["user"]["login"])
    return list(set(result))


def concerened_reviewers(GITHUB_URL, GITHUB_TOKEN, concerened_file=None):
    pull_numbers = get_pull_numbers(GITHUB_URL, GITHUB_TOKEN)
    res = {}
    for i, pull_number in enumerate(pull_numbers):
        print(i, "/", len(pull_numbers))
        reviewers = get_reviewers(GITHUB_URL, GITHUB_TOKEN, pull_number, concerened_file=concerened_file)
        for reviewer in reviewers:
            if reviewer not in res:
                res[reviewer] = 1
            else:
                res[reviewer] += 1
    return res


if __name__ == "__main__":
    GITHUB_TOKEN = USER.GITHUB_TOKEN
    GITHUB_URL = USER.GITHUB_URL
    concerened_file = USER.CONCERNED_FILE
    print(concerened_reviewers(GITHUB_URL, GITHUB_TOKEN, concerened_file=concerened_file))
