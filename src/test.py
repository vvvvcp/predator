from pygerrit.rest import GerritRestAPI
import sys
from debian.changelog import change
from requests.exceptions import RequestException
rest = GerritRestAPI(url='http://review.cyanogenmod.org')
query_url ="/changes/?q=owner:%s+status:merged"
def tm_query(email):
    try:
        final_url=query_url%email
        change=rest.get(final_url)
        print email,len(change)
    except RequestException as err:
        print email,0
if __name__ == '__main__':
    f=open('all.txt','r')
    lines=f.readlines()
    for line in lines:
        tm_query(line)
    f.close()
