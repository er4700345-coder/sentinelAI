from github import Github

class GithubBot:

    def __init__(self, token):
        self.client = Github(token)

    def create_issue(self, repo_name, title, body):

        repo = self.client.get_repo(repo_name)

        issue = repo.create_issue(
            title=title,
            body=body
        )

        return issue.html_url
