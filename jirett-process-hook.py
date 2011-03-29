#!/usr/bin/python
#
# Refer to the XML-RPC Javadoc to see what calls are available:
# http://docs.atlassian.com/software/jira/docs/api/rpc-jira-plugin/latest/com/atlassian/jira/rpc/xmlrpc/XmlRpcService.html
 
import xmlrpclib
import sys
import ConfigParser
import commands
import re

# Gerrit command
gerrit_cmd = "ssh gerrit gerrit"

config = ConfigParser.RawConfigParser()
config.read('jirett.ini')

user = config.get('jira', 'user')
password = config.get('jira', 'pass')
url = config.get('jira', 'url')

rpc = xmlrpclib.ServerProxy(url)
auth = rpc.jira1.login(user, password)

def showUsage():
    print '\nNormal hook usage: ' + sys.argv[0] + ' [new|merged|abandoned] <change id> <url to change>'
    print '\nTo automatically update projects list in config: ' + sys.argv[0] + ' update-projects'

def updateProjects():
    projects = rpc.jira1.getProjectsNoSchemes(auth)
    s = ''
    for p in projects:
        s += p['key'] + ','

    s = s.rstrip(',')
    config.set('jira', 'projects', s)

    with open('jirett.ini', 'wb') as configfile:
        config.write(configfile)
        
    print '\nAdded "' + s + '" to jirett.ini.\n'

def updateTicket(what, id, url):
    status, out = commands.getstatusoutput(gerrit_cmd + ' query --format TEXT change:' + id + ' limit:1')
    if (status != 0):
        print 'Could not run gerrit query command.\n' + out
        exit()
    subject = re.search('subject:.*[^\n]', out).group();
    projects = config.get('jira', 'projects').split(',')

    for p in projects:
        match = re.search('subject:.*(' + p + '-[0-9]+).*', subject).groups()[0]
        if (len(match) > 0):
            break
    if (len(match) > 0):
        if what == 'new':
            message = 'New patchset uploaded'
        elif what == 'merged':
            message = 'Change merged'
        elif what == 'abandoned':
            message = 'Changset abandonded'
        else:
            print 'Illegal argument, stopping: ' + what
            exit()

        message += ' (' + id + ') at ' + url  
        rpc.jira1.addComment(auth, match, message)
        exit()


def main():

    if (len(sys.argv) < 2):
        showUsage()
        exit()

    if (sys.argv[1] == 'update-projects'):
        updateProjects()
        exit()

    if (len(sys.argv) != 4):
        showUsage()
        exit()

    what = sys.argv[1]
    id = sys.argv[2]
    url = sys.argv[3]

    if (len(what) > 0 and len(id) > 0 and len(url) > 0):
        updateTicket(what, id, url)
    else:
        showUsage()
        
if __name__ == '__main__':
    main()




 
