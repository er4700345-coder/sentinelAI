import subprocess

class StaticAnalyzer:

    def scan(self, repo_path):
        result = subprocess.run(
            ["bandit", "-r", repo_path, "-f", "json"],
            capture_output=True,
            text=True
        )

        return result.stdout
