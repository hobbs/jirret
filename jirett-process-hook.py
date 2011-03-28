#!/usr/bin/python
#
# Refer to the XML-RPC Javadoc to see what calls are available:
# http://docs.atlassian.com/software/jira/docs/api/rpc-jira-plugin/latest/com/atlassian/jira/rpc/xmlrpc/XmlRpcService.html
 
import xmlrpclib
import sys

#s = xmlrpclib.ServerProxy('http://jira.atlassian.com/rpc/xmlrpc')
s = xmlrpclib.ServerProxy('http://jira.tunewiki.net/rpc/xmlrpc')
auth = s.jira1.login('zach', 'droid1')

def showUsage():
    print '\nUsage: ' + sys.argv[0] + ' [new|merged|abandoned] <change id>\n\n'

if (len(sys.argv) != 3):
    showUsage()
    exit();


s.jira1.addComment(auth, "SMPA-70", 'Comment added with XML-RPC')
 
print "Done!"
