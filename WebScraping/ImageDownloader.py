from bs4 import BeautifulSoup
import requests
import sys
import os

# This program when given the url of a thread on 4chan will download all the images from that thread into the IMAGES folder
# The URL is passed as a command line parameter

# Check for enough arguments 
if len(sys.argv) < 2:
    print('Not enough arguments to run')
    exit()

# Repeat for all urls in the list
folderCount = 1
for url in sys.argv[1:]:
    # Make the directories
    os.makedirs('IMAGES/' + str(folderCount))

    # Get the page
    page = requests.get(url)
    content = page.content
    soup = BeautifulSoup(content, features = 'html.parser')

    # identify all the image links on the page
    imageLinks = [a['href'] for a in soup.find_all('a', class_='fileThumb')]

    # Download all the image links
    total = len(imageLinks)
    print (str(total) + ' images found')
    count = 0
    for image in imageLinks:
        r = requests.get('http:' + str(image))
        filename = image.split('/')[-1]
        open('IMAGES/' + str(folderCount) + '/' + filename, 'wb').write(r.content)
        count = count + 1
        print('completed ' + str(count) + '/' + str(total))
    folderCount = folderCount + 1