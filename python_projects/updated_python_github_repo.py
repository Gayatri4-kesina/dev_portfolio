import requests
import operator
from datetime import datetime, timedelta, timezone
import logging

logging.basicConfig(
    filename='/var/log/repo.log',
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)


class GitHubAPI:
    def __init__(self, token: str = None) -> None:
        self.base_url = "https://api.github.com"
        self.headers = {"Accept": "application/vnd.github.v3+json"}
        if token:
            self.headers["Authorization"] = f"Bearer {token}"

    def get_user(self, username: str) -> dict:
        try:
            response = requests.get(
                f"{self.base_url}/users/{username}",
                headers=self.headers,
                timeout=5
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to get user {username}: {e}")
            raise

    def get_repos(self, username: str) -> list:
        try:
            response = requests.get(
                f"{self.base_url}/users/{username}/repos",
                headers=self.headers,
                params={"per_page": 100, "sort": "updated"},
                timeout=5
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to get repos for {username}: {e}")
            raise

    def get_starred_repos(self, username: str) -> list:
        try:
            response = requests.get(
                f"{self.base_url}/users/{username}/starred",
                headers=self.headers,
                timeout=5
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to get starred repos for {username}: {e}")
            raise


def analyze_languages(repos: list) -> dict:
    languages = {}
    for repo in repos:
        if repo['language']:
            languages[repo['language']] = languages.get(repo['language'], 0) + 1
    return languages


def get_recent_repos(repos: list, days: int = 180) -> list:
    current_date = datetime.now(timezone.utc)
    cutoff = current_date - timedelta(days=days)
    recent = []
    for repo in repos:
        created = datetime.fromisoformat(repo['created_at'].replace('Z', '+00:00'))
        if cutoff <= created <= current_date:
            recent.append(repo['name'])
    return recent


def main():
    github = GitHubAPI()
    username = input("Enter GitHub username: ")

    try:
        # fetch data
        user = github.get_user(username)
        repos = github.get_repos(username)
        starred = github.get_starred_repos(username)

        # analyze
        languages = analyze_languages(repos)
        most_used_lang = max(languages.items(), key=operator.itemgetter(1))[0] if languages else "N/A"
        most_starred = max(repos, key=lambda r: r['stargazers_count']) if repos else None
        recent_repos = get_recent_repos(repos)

        # display
        report_lines = [
            f"===== GitHub Profile Report: {username} =====",
            f"Name: {user.get('name', 'N/A')}",
            f"Bio: {user.get('bio', 'N/A')}",
            f"Followers: {user['followers']}",
            f"Following: {user['following']}",
            f"Total Repos: {len(repos)}",
            f"Total Starred: {len(starred)}",
            f"Most Used Language: {most_used_lang}",
            f"Most Starred Repo: {most_starred['name']} {most_starred['stargazers_count']}" if most_starred else "No repos",
            f"\nRepos Created in Last 6 Months ({len(recent_repos)}):",
        ] + recent_repos

        # print and write to file
        for line in report_lines:
            print(line)

        with open("github_report.txt", "w") as f:
            f.write("\n".join(report_lines))

        logging.info(f"Report generated for {username}")
        print("\nReport saved to github_report.txt")

    except requests.exceptions.ConnectionError:
        print("No internet connection")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
    except Exception as e:
        print(f"Error: {e}")
        logging.error(f"Error analyzing {username}: {e}")


if __name__ == "__main__":
    main()
