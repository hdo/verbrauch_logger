import urllib2, re, ConfigParser, os
import datetime as datetime

def getOutputDir():
   config = ConfigParser.RawConfigParser()
   if not os.path.exists('config.ini'):
      return None
   config.read('config.ini')
   if not config.has_section('main') or not config.has_option('main','output'):
      return None
   p = config.get('main', 'output')
   if not os.path.exists(p):
      os.makedirs(p)
   return p
   
def getMethod():
   config = ConfigParser.RawConfigParser()
   if not os.path.exists('config.ini'):
      return None
   config.read('config.ini')
   if not config.has_section('main') or not config.has_option('main','method'):
      return None
   ret = config.get('main', 'method')
   return ret

def getJsonFile():
   config = ConfigParser.RawConfigParser()
   if not os.path.exists('config.ini'):
      return None
   config.read('config.ini')
   if not config.has_section('main') or not config.has_option('main','json'):
      return None
   ret = config.get('main', 'json')
   return ret

def getJsonUrl():
   config = ConfigParser.RawConfigParser()
   if not os.path.exists('config.ini'):
      return None
   config.read('config.ini')
   if not config.has_section('main') or not config.has_option('main','url'):
      return None
   ret = config.get('main', 'url')
   return ret
   
def getLogFile():
   year = datetime.datetime.now().year
   return "%d.log" % year      
   
def getCurrentTimeStamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def getLogDataFromWeb(url):
   tempSite = urllib2.urlopen(url).read()
   return tempSite.replace('\r\n','')

def getLogDataFromFile(f):
   tempSite = open(f).read()
   return tempSite.replace('\n','')

def appendFile(f, data):
   f = open(f, "a")
   f.write(data + "\n")
   f.close()

if not getOutputDir() or not getMethod():
   print "exit!"
   exit()
       
if getMethod().lower() == 'file':
   data = getLogDataFromFile(getJsonFile())
if getMethod().lower() == 'web':
   data = getLogDataFromWeb(getJsonUrl())

if data:
   logfile = os.path.join(getOutputDir(), getLogFile())
   logentry =  "%s %s" % (getCurrentTimeStamp(), data)
   appendFile(logfile, logentry)

