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

# approve になって自分がレビューしたもの
# https://api.github.com/search/issues?q=is:pr+review:approved+reviewed-by:YoshinoriN

# あるファイルに関わったPRを全て取得する

# あるファイルに関わった人間を全て取得する

# "https://api.github.com/repos/Lennethe/github_api/issues/3/comments"

    

command = ["issues", "pulls?state=all", "issues/3/comments"]
lists = get_url(command[1])


print(lists)
