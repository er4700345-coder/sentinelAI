from sentinel.repo_loader import RepoLoader
from sentinel.static_analyzer import StaticAnalyzer
from sentinel.ai_detector import AIDetector
from sentinel.report_generator import ReportGenerator
from sentinel.github_bot import GithubBot

def main():

    repo_url = input("Repository URL: ")

    loader = RepoLoader(repo_url)
    path = loader.clone()

    analyzer = StaticAnalyzer()
    static_report = analyzer.scan(path)

    with open(__file__) as f:
        code = f.read()

    ai = AIDetector(api_key="YOUR_KEY")
    ai_report = ai.analyze(code)

    generator = ReportGenerator()
    report = generator.generate(static_report, ai_report)

    print(report)

if __name__ == "__main__":
    main()
