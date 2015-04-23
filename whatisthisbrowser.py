from bs4 import BeautifulSoup
import requests
import sys

user_agent = sys.argv[1]
print 'Looking for User-Agent: %s' % user_agent

req = requests.get('https://www.whatismybrowser.com/developers/custom-parse?useragent=%s' % user_agent)
soup = BeautifulSoup(req.content)
try:
	print soup.find('div', attrs={'class': 'string-major'}).text
except:
	print 'This has not been found on the website.'