#!/usr/bin/env python3

#could use Requests-HTML instead of beautiful soup (uses less code)

from bs4 import BeautifulSoup
import requests

site_url = requests.get("https://www.trademe.co.nz/a/search")

def main():
    """main function"""
    soup = BeautifulSoup(site_url.text, "html.parser")
    print(soup.title)
    get_tm_data(soup)

def get_tm_data(soup):
    listings = soup.find()
    listings_rows = [row for row in listings.contents if row != "\n"]
    print(listings_rows)

if __name__ == '__main__':
    main()
    
    