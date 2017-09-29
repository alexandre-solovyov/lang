
import urllib2
import os

#for k in os.environ.keys():
#    if 'HTTP' in k:
#        print k

#req = urllib2.Request('http://www.google.com')
#req = urllib2.Request('http://www.lingvo-online.ru/ru/Translate/fr-ru/parler')
#req = urllib2.Request('https://translate.yandex.ru/?text=parler&lang=fr-ru')

ya_key = 'trnsl.1.1.20160713T184532Z.21e3d808b2dad386.898fb39b231456322fa385d108e44fe0606619f8'
ya_lang = 'fr-ru'
ya_text = "apprendre"
 
ya_link = "https://translate.yandex.net/api/v1.5/tr.json/translate?key=%s&text=%s&lang=%s" % ( ya_key, ya_text, ya_lang )
req = ya_link

print req
response = urllib2.urlopen(req)
the_page = response.read()
print the_page
