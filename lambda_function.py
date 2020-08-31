from github import Github

git = Github("yogeshvedpathak", "gW!ndyc1ty")
#git = Github(login_or_token="5d20a9283c7d76504e8968a448fda140d15b046b")
for repo in git.get_user().get_repos():
    print(repo.name)
    repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    print(dir(repo))
