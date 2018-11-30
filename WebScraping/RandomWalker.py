from bs4 import BeautifulSoup
from urlparse import urlparse
import requests
import sys
import random

# Check for enough arguments 
if len(sys.argv) < 2:
    print('Not enough arguments to run')
    exit()

# Keep looking at pages FOR EVER
urlToCheck = sys.argv[1]
while True:
    # Get a page
    url = urlparse(urlToCheck)
    page = requests.get(urlToCheck)
    content = page.content
    soup = BeautifulSoup(content, features = 'html.parser')

    # Print some info
    print('Title: ' + soup.title.string)
    print('HostName: ' + url.netloc)

    # Get all the links
    imageLinks = soup.find_all('a')

    # Pick a random link to use next
    goodChoice = False
    choice = ''
    while not goodChoice:
        choice = random.choice(imageLinks)['href']
        if not choice.startswith('javascript'):
            goodChoice = True
            print(choice)