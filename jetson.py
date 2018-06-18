#!/usr/bin/env python

import argparse
import requests


def call_api(args):
    base_url = args.api
    max_pages = args.maxpages
    page = 1
    per_page = args.projects or 5
    expected_status_code = 200
    has_next = True
    data = []

    while has_next:
        req_url = '{0}?page={1}&per_page={2}'.format(base_url, page, per_page)
        response = requests.get(req_url)
        status_code = response.status_code
        if status_code != expected_status_code:
            break
        page += 1
        json = response.json()
        for repo in json:
            print(repo['http_url_to_repo'])
            data.append(repo['http_url_to_repo'])
        if page > max_pages:
            has_next = False


def main():
    parser = argparse.ArgumentParser(description='Project Auditor searching for some leaks')
    parser.add_argument('--api', help='Repo API to scrape', default='https://gitlab.com/api/v4/projects')
    parser.add_argument('--projects', type=int, help='number of repositories to search', default=5)
    parser.add_argument('--maxpages', type=int, help='max number of pages to request', default=3)
    args = parser.parse_args()
    print('Jetting off to generate a list of repositories')
    call_api(args)


if __name__ == '__main__':
    main()
