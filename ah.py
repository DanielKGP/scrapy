from bs4 import BeautifulSoup
import urllib2
import re

urllist = []
urllist2 = []
title = []
def grabHref(url):

    html = urllib2.urlopen(url).read()
    html = unicode(html,'gb2312','ignore').encode('utf-8','ignore')
    soup = BeautifulSoup(html,"html.parser")
    title.append(soup.title.string)

    content = BeautifulSoup(html,"html.parser").findAll('a')

    pat = re.compile(r'href="([^"]*)"')
    pat2 = re.compile(r'http')
    count = 20
    for item in content:
        h = pat.search(str(item))
        href = h.group(1)
        if pat2.search(href):
            ans = href
        else:
            ans = url+href

        if ans == url:
            pass
        else:
            urllist.append(ans)
            count -= 1
        if count == 0:
            break

def grab(url):

    html = urllib2.urlopen(url).read()
    html = unicode(html,'gb2312','ignore').encode('utf-8','ignore')
    soup = BeautifulSoup(html,"html.parser")

    title.append(soup.title.string)



url = "http://english.sina.com/news/entertainment/"


grabHref(url)

urllist = list(set(urllist))

while urllist:
    temp = urllist.pop()
    urllist2.append(temp)
    grab(temp)

while urllist2:
    grabHref(urllist2.pop())


title = list(set(title))
print title

while title:
    titlefile = open('title.txt','a')
    titlefile.write(title.pop()+'\n')

titlefile.close()
