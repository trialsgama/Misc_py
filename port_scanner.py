import optparse
import socket
from socket import *
def main():
    parser=optparse.OptionParser('usage %prog -H'+ ' <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost',type='string',help='Specify target host')
    parser.add_option('-p',dest='tgtPort',type='string',help='Specify target port')
    (options, args)=parser.parse_args()
    tgtHost=options.tgtHost
    tgtPort=options.tgtPort
    if (tgtHost == None) | (tgtPort == None):
        print parser.usage
        exit(0)
    connScan(tgtHost,tgtPort)
def connScan(tgtHost,tgtPort):
    try:
        tgtIP = gethostbyname(tgtHost)
        connSkt= socket(AF_INET,SOCK_STREAM)
        tgtPort=int(tgtPort)
        connSkt.connect((tgtIP,tgtPort))
        print '[+]%d/tcp open'% tgtPort
        connSkt.close()
    except:
        print '[-]%d/tcp closed'% tgtPort
if __name__=='__main__':
    main()

