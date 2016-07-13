
import urllib2
import os

for k in os.environ.keys():
    if 'HTTP' in k:
        print k

req = urllib2.Request('http://www.google.com')
response = urllib2.urlopen(req)
the_page = response.read()
print the_page
