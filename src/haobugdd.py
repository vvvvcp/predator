# -*- coding: UTF-8 -*-
import sys
import re
import urllib2
from bs4 import BeautifulSoup
from pyasn1.compat.octets import null
reload(sys)
sys.setdefaultencoding('utf-8')


if __name__ =='__main__':
    bugid=re.compile("\d{5}")
    f=open('gitlog.txt','r')
    file_write = open('loglist.txt','w+')
    lines=f.readlines()
    for line in lines:
       if "[id]" in line:
           print line,
           id=bugid.findall(line)
           if len(id):
               print id[0]
               haobug="http://10.120.10.150/bugzilla/show_bug.cgi?id="+id[0]
               print haobug,
               data=urllib2.urlopen(haobug)
               result=BeautifulSoup(data.read())
           #print result.title
               print (id[0]+" "+result.title.string)
               file_write.write(result.title.string)
               file_write.write("\n")
    f.close()
    file_write.close()