from bs4 import BeautifulSoup
import requests
import sys

# Check for enough arguments 
if len(sys.argv) < 2:
    print('Not enough arguments to run')
    exit()

