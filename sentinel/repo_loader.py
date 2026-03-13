import os
from git import Repo

class RepoLoader:
    def __init__(self, repo_url, path="repos"):
        self.repo_url = repo_url
        self.path = path

    def clone(self):
        name = self.repo_url.split("/")[-1]
        target = os.path.join(self.path, name)

        if not os.path.exists(self.path):
            os.makedirs(self.path)

        if not os.path.exists(target):
            Repo.clone_from(self.repo_url, target)

        return target
