import re
import urllib.request

html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()

print (html)
