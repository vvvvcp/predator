# -*- coding: UTF-8 -*-
import sys
import re
import urllib2
from bs4 import BeautifulSoup
from pyasn1.compat.octets import null
reload(sys)
sys.setdefaultencoding('utf-8')


if __name__ =='__main__':
	m = lambda x:x*2
	print m(3),
	print m(4),
	n = lambda x,y,z: (x-y)*z
	print n(2,4,3)
