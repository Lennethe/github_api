from github import Github

# First create a Github instance:

# or using an access token
g = Github("access_token")

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)
