import optparse
import requests,urllib
from bs4 import BeautifulSoup
def main():
    parser=optparse.OptionParser('usage %prog -q'+ ' <google search query>')
    parser.add_option('-q', dest='query',type='string',help='Specify google search query')
    (options, args)=parser.parse_args()
    query=options.query
    if (query == None):
        print parser.usage
        exit(0)
    GoogleSearch(query)
def GoogleSearch(query):
    query=query.replace(' ','+')
    print query
    URL="https://google.com/search?q=" + query +""
    print URL
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {"user-agent":USER_AGENT}
    resp = requests.get(URL,headers=headers)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content,"html.parser")
        results=[]
        for g in soup.findAll('div',class_='r'):
            anchors= g.findAll('a')
            if anchors:
                results.append(anchors[0]['href'])
        for x in results:
            print x
if __name__=='__main__':
    main()
    