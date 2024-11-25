"""Demonstrates basic Beautiful Soup 4 Ops.
"""

from bs4 import BeautifulSoup
import requests


def get_html(url):
    r = requests.get(url)
    return r.text

def create_soup(html_text):
    return BeautifulSoup(html_text, 'html.parser')
    

def main():
    while True:
        url = input('Enter URL to scrape: ')
        try:
            soup = create_soup(get_html(url))
            print(soup.prettify())
            h3s = soup.find_all('h5')
            print(h3s)
            for h in h3s:
                print(h)
        except Exception as e:
            print(f'Problem scraping {url}: {e}')

if __name__ == '__main__':
    main()