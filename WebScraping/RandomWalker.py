from bs4 import BeautifulSoup
import urlparse
import requests
import sys
import random

# Check for enough arguments 
if len(sys.argv) < 2:
    print('Not enough arguments to run')
    exit()

# Keep looking at pages FOR EVER
prevUrl = ''
urlToCheck = sys.argv[1]
while True:

    # Get a page
    url = urlparse.urlparse(urlToCheck)
    page = requests.get(urlToCheck)
    content = page.content
    soup = BeautifulSoup(content, features = 'html.parser')

    # Print some info
    if soup.title:
        print('Title: ' + soup.title.string)
    print(urlToCheck)
    print('HostName: ' + url.netloc + '\n')

    # Get all the links
    imageLinks = soup.find_all('a')

    # Check if there are any links on the page
    if len(imageLinks) == 0:
        urlToCheck = prevUrl
        # Check if it was the first link
        if urlToCheck == '':
            print('\nURL had no links')
            exit()
        continue
        
    prevUrl = urlToCheck

    # Pick a random link to use next
    # Remove bad links first
    validLinks = [a for a in imageLinks if not a["href"].startswith('javascript') and not a["href"].startswith('#')]
    choice = random.choice(validLinks)['href']
    
    # Make absolute url from relative path found
    urlToCheck = urlparse.urljoin(urlToCheck, choice)