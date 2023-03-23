import requests
from bs4 import BeautifulSoup
import csv

def request_github_trending(url):
    return requests.get(url)

def extract(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    html_repos = soup.find_all('article', {'class': 'Box-row'})
    return html_repos

def transform(html_repos):
    repositories_data = []
    for repo in html_repos:
        developer = repo.find('span', {'class': 'text-normal'}).text.strip()
        repository_name = repo.find('h1', {'class': 'h3 lh-condensed'}).text.strip()
        nbr_stars = repo.find('a', {'class': 'Link--muted d-inline-block mr-3'}).text.strip()
        repositories_data.append({'developer': developer, 'repository_name': repository_name, 'nbr_stars': nbr_stars})
    return repositories_data

def format(repositories_data):
    csv_string = 'Developer,Repository Name,Number of Stars\n'
    for repo in repositories_data:
        csv_string += repo['developer'] + ',' + repo['repository_name'] + ',' + repo['nbr_stars'] + '\n'
    return csv_string

def main():
    url = 'https://github.com/trending'
    page = request_github_trending(url)
    html_repos = extract(page)
    repositories_data = transform(html_repos)
    csv_string = format(repositories_data)
    print(csv_string)

if __name__ == '__main__':
    main()
