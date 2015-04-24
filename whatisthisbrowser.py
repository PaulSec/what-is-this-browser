#!/bin/env python
# -*- cofing: utf-8 -*-

from __future__ import print_function, unicode_literals

import requests
import sys

try:
    from bs4 import BeautifulSoup
except ImportError as e:
    sys.exit('Error: BeautifulSoup4 has not been found on your system!')


UA_URL = 'https://whatismybrowser.com/developers/custom-parse?useragent={0}'


def usage():
    '''Return a usage message for this program.'''
    return 'Usage: {cmd} "USER AGENT"'.format(cmd=sys.argv[0])


def get_information(user_agent):
    '''Get and return information about given user agent.'''

    req = requests.get(UA_URL.format(user_agent))
    soup = BeautifulSoup(req.content)

    try:
        return soup.find('div', attrs={'class': 'string-major'}).text
    except AttributeError:
        return 'This has not been found on the website.'


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(usage())

    user_agent = sys.argv[1]
    print('Looking for User-Agent: {0}'.format(user_agent))
    print(get_information(user_agent))
