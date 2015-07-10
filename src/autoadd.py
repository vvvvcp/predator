import sys
from pygerrit.rest import GerritRestAPI
import urllib2
import urllib
from requests.auth import HTTPBasicAuth, HTTPDigestAuth
from requests.exceptions import RequestException
#reload(sys)
#sys.setdefaultencoding('utf-8')
gerrit_url='http://review.cyanogenmod.org/'
post='/changes/Ic284c9074e2bfb283dc5d59050e7344b009b5441/reviewers'
#rest = GerritRestAPI(url=gerrit_url,auth='xiao.hu',)

def post_add(changid,email):
    auth = HTTPBasicAuth('xiao.hu', '123456')
    rest = GerritRestAPI(url=gerrit_url)
    post_url=post
    #"reviewer": "john.doe@example.com"
    test_data = {'reviewer':'yadong.huang@ck-telecom.com'}
    try: 
        change=rest.post(post_url, data=test_data)
        print change
    except RequestException as err:
        print err
if __name__=='__main__':
    post_add(sys.argv[1], 'yadong.huang@ck-telecom.com')
    #test_data = {'reviewer': 'yadong.huang@ck-telecom.com'}
    #test_data_urlencode = urllib.urlencode(test_data)

    #requrl = "http://192.168.81.16/cgi-bin/python_test/test.py"
    #post_url=gerrit_url%sys.argv[1]

    #req = urllib2.Request(url = post_url,data =test_data_urlencode)
    #print req

    #res_data = urllib2.urlopen(req)
    #res = res_data.read()
    #print res