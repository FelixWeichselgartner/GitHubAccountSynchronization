import os
from github import Github
#https://github.com/PyGithub/PyGithub
#https://pygithub.readthedocs.io/en/latest/index.html
from GetFolders import get_folders
from api_token import mytoken

g = Github(mytoken)

#print(g.get_user().get_repos())
#print()
mpath = os.path.join(os.getcwd(), 'my_repos')
mfolders = get_folders(mpath)
#print(mfolders)
spath = os.path.join(os.getcwd(), 'starred_repos')
sfolders = get_folders(spath)
#print(sfolders)

def clone_and_pull(repos, thepath, currfolder):
    for repo in repos:
        print()
        print(repo.name)
        if repo.name in currfolder:
            print('Repository is already available -> pulling')
            os.system(f'cd {thepath}/{repo.name}/ && git pull origin master')
        else:
            print('Repository not available -> cloning')
            os.system(f'cd {thepath}/ && git clone {repo.clone_url}')

# My repos
"""for repo in g.get_user().get_repos():
    print(repo.name)
    print(repo.description)
    print(f'stars: {repo.stargazers_count}')
    print(f'language: {repo.language}')
    print(f'size: {repo.size}kB')
    print(f'created at: {repo.created_at}')
    print()"""
my_repos = g.get_user().get_repos()
clone_and_pull(my_repos, 'my_repos', mfolders)


# starred repos
s_repos = g.get_user().get_starred()
clone_and_pull(s_repos, 'starred_repos', sfolders)
