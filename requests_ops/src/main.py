""" Demonstrates the use of the requests library.

	The requests library is a third-party package 
    available from The Python Package Index (PyPI)
    https://pypi.org
    
"""

import requests
import sys



def show_website_info(url):
    r = requests.get(url)
    print(r.text)



def main():
    while True:
        try:
            website = input('Enter website url: ')
            if website.lower() == 'quit': 
                sys.exit()
            show_website_info(website)
        except Exception as e:
            print(f'Problem accessing website. {e}')
    

if __name__ == '__main__':
    main()

