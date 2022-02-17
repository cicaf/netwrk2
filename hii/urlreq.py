from urllib import response
from urllib.request import urlopen

from httplib2 import Response
response = urlopen('http://www.debian.org')
response
response.readline()
response.getheaders()