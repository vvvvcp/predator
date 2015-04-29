#!/usr/bin/python
import sys
from ubuntu_sso.utils.ui import TITLE
from cupshelpers.config import prefix
from time import sleep
from duplicity.backend import retry
from cherrypy import request, response
from orca.braille import Link
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2, socket, time
import gzip, StringIO
import re, random, types

from bs4 import BeautifulSoup

base_url='http://www.googleta.com/'
results_per_page=10

user_agents =list ()

class SearchResult:
    def __init__(self):
        self.url=''
        self.title=''
        self.content=''
    def getURL(self):
        return self.url
    def setURL(self,url):
        self.url=url
    def getTitle(self):
        return self.title
    def setTitle(self,title):
        self.title=title
    def getContent(self):
        return self.content
    def setContent(self,content):
        self.content=content
    def printIt(self,prefix=''):
        f.GGwrite('url->'+self.url+'\n'+'title->'+self.title+'\n'+'content->'+self.content+'/n')
        print
        print 'url\t->',self.url
        print 'title\t->',self.title
        print 'content\t->',self.content
        print
    def writeFile(self,filename):
        file = open(filename,'a')
        try:
            file.write('url:'+self.url+'\n')
            file.write('title:'+self.title+'\n')
            file.write('content:'+self.content+'\n\n')
        except IOError,e:
            print 'file error:',e
        finally:
            file.close()
class GoogleAPI:
    def __init__(self):
        timeout = 40
        socket.setdefaulttimeout(timeout)
    def randomSleep(self):
        sleeptime = random.randint(60,120)
        time.sleep(sleeptime)
    def extractDomain(self,url):
        domain =''
        pattern =re.compile(r'http[s]://([^/]+)/', re.U|re.M)
        url_match = pattern.search(url);
        if(url_match and url_match.lastindex >0):
           domain = url_match.group(1)
        return domain
    def extractUrl(self,href):
        url=''
        pattern=re.compile(r'(http[s]?://[^&]+)&', re.U|re.M)
        url_match=pattern.search(href)
        if(url_match and url_match.lastindex > 0):
            url= url_match.group(1)
        return url
    def extractSearchResults(self,html):
        result = list()
        soup =BeautifulSoup(html)
        div = soup.find('div', id  = 's')
        if(type(div)!=types.NoneType):
            lis=div.findall('li',{'class':'g'})
            if(len(lis)>0):
                for li in lis:
                    result=SearchResult();
                    h3 = li.find('h3',{'class':'r'})
                    if(type(h3)==types.NoneType):
                        continue
                    link = h3.find('a')
                    if(type(link)==types.NoneType):
                        continue
                    url=link['href'];
                    url=self.extractUrl(url)
                    if(cmp(url,'')==0):
                        continue
                    title=link.renderContents()
                    result.setURL(url)
                    result.setTitle(title)
                    span=li.find('span',{'class':'st'})
                    if(type(span)!=types.NoneType):
                        content=span.renderContents()
                        result.setContent(content)
                    result.append(result)
        print "finish extraction!"
        return result
    def search(self,query,lang='en'):
        search_results=list()
        query=urllib2.quote(query)
        for s in range(3):
            url='%s/s?wd=%s::q:q
            '%(base_url,query)
            print url
            retry=3
            while(retry>0):
                try:
                    request=urllib2.Request(url)
                    length=len(user_agents)
                    index=random.randint(0,length-1)
                    user_agent=user_agents[index]
                    request.add_header('User-agent',user_agent)
                    request.add_header('connection','keep-ali:qve')
                    request.add_header('Accept-Encoding','gzip')
                    request.add_header('referer',base_url)
                    response=urllib2.urlopen(request)
                    html=response.Read()
                    print "read!"
                    if(response.headers.get('content-encoding',None)=='gzip'):
                        html=gzip.GzipFile(fileobj=StringIO.StringIO(html)).read()
                    results=self.extractSearchResults(html)
                    search_results.extend(results)
                    break;
                except urllib2.URLError,e:
                    print 'url error:',e
                    self.randomSleep()
                    retry=retry-1
                    continue
                except Exception,e:
                    print 'error:',e
                    retry=retry -1
                    self.randomSleep()
                    continue
        return search_results
def load_user_agent():
    fp=open('./user_agents','r')
    line =fp.readline().strip('\n')
    while(line):
        user_agents.append(line)
        line=fp.readline()
    fp.close()
def crawler():
    load_user_agent()
    api=GoogleAPI()
    if(len(sys.argv)<2):
        keywords=open('./keywords','r')
        keyword=keywords.readline()
        while(keyword):
            results=api.search(keyword)
            for r in results:
                r.printIt()
            keyword=keywords.readline()
        keywords.close()
    else:
        keywords=sys.argv[1]
        results=api.search(keywords)
        cur=1
        URLs=[]
        for r in results:
            if r.getGGURL() not in URLs:
                print str(cur)+'.',
                f.write(str(cur)+'.')
                cur+=1
                r.printIt()
                URLs+=[r.getURL()]
if __name__=='__main__':
    f=open('result.txt','w')
    print "huxiao"
    crawler()
    f.close()
