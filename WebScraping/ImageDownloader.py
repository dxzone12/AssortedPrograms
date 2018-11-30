from bs4 import BeautifulSoup
import requests
import sys

# This program when given the url of a thread on 4chan will download all the images from that thread into the IMAGES folder
# The URL is passed as a command line parameter

# Check for enough arguments 
if len(sys.argv) < 2:
    print('Not enough arguments to run')
    exit()

# Get the page
page = requests.get(sys.argv[1])
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
    open('IMAGES/' + filename, 'wb').write(r.content)
    count = count + 1
    print('completed ' + str(count) + '/' + str(total))