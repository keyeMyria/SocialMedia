# -*- coding: utf-8 -*-

import urllib2,bs4,sys,resource,os,json
from time import time

print "[*] resource limit :",resource.getrlimit(resource.RLIMIT_STACK)
print "[*] recursion limit ",sys.getrecursionlimit()
print "[*] setting recursion limit to twice the usuel /!\ : ", 0x100000 #1048576 

resource.setrlimit(resource.RLIMIT_STACK, [0x100000, resource.RLIM_INFINITY])
sys.setrecursionlimit(0x100000)

class crawl(object):
    def __init__(self,path=None):
     self.path   = path
     self.start  = 0
     self.max_depth  = 0
     self.urls   = {}
     self.root_u = ''
     self.m_name = ''
     self.m_url  = ''
     self.agent  = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) \
	Chrome/35.0.1916.47 Safari/537.36'
     self.logs   = True
     self.opener = urllib2.build_opener()
     self.opener.addheaders = [('User-Agent', self.agent)]
    def _clean(self):
       for k in self.urls.keys():
         if self.urls[k] == True:
     	   del self.urls[k]
    def _check_depth(self):
      if len(self.urls)>self.max_depth:
        return False
      else:
        return True
    def _new_element(self):
    	val = self.urls.values()
    	if len(val) ==0:
    		return None
    	if len(set(val)) ==1 and val[0]==True:
    		return None
    	else:
    	  for k in self.urls.keys():
    	    if self.urls[k]== False:
    		return k
    def _pages(self,page):
      """page is bs4 object """
      for i in page.find_all('a'):
        elm =i.get('href','').encode('ascii',errors='ignore')
        #if elm.startswith('www') and not(self.root_u in elm):
         # continue
        if elm.startswith('/') or (not(self.m_name in elm) and not('www' in elm)):
          elm = self.root_u + elm 
        #if self.m_name in elm:
        if self.urls.get(elm,False)==False  :
           self.urls[elm] = False
           print '\x1b[1;31;40m'+"[*]"'\x1b[0m'," new url :\x1b[0;32;40m%s\x1b[0m --> dict size \x1b[0;34;40m%s\x1b[0m"%(elm[len(self.root_u):],str(len(self.urls.keys())))

       
    def _agent(self,agent=None):
       if agent:
	 self.agent = agent
	 self.opener.addheaders = [('User-Agent', agent)]
       else:
   	 return self.agent
    def _thread(self,url):
      new =self._new_element()
      if new:
          self.urls[url] = True
          self._crawl(new)
      else:
          print "\n".join(self.urls.keys())
          print "[*] operations done in %s . S "%(time()-self.start)      

    def _crawl(self,url):
        try:
          if self._check_depth():
            print "\x1b[0;31;40m[*] getting webpage : \x1b[0m"	,url
            page = self.opener.open(url).read()
            self._pages(bs4.BeautifulSoup(page,'html5lib'))
            self._thread(url) 
        except Exception as e:
            #self._save_xml()
            print "[-] erro was detected  -->",e
            self._thread(url)

    def run(self,m_url,max_depth):
        self.max_depth=max_depth
        self.m_url  = m_url
        self.m_name = m_url.split('://')[1].split('.')[1]
        self.protoc = m_url.split('://')[0]+"://"
        l = m_url.split('://')[1].split('.')
        self.root_u = self.protoc+l[0]+'.'+l[1]+'.'+l[2].split('/')[0]+'/'
        self._crawl(m_url)
    def _save_json(self):
      f= open(self.path,'w+')
      tmp ={}
      for k,i in enumerate(self.urls.keys()):
      	tmp[k] = i
      json.dump(tmp,f)
      f.close()
    def main_save(self):
    	if 'json' in self.path:
    		self._save_json()
    	else:
    		self._save_xml()
    def main_ret(self):
      tmp ={}
      for k,i in enumerate(self.urls.keys()):
        tmp[k] = i
      return tmp
    def _save_xml(self):
      from xml.dom import minidom
      temple = """ 
    <data>
    <sub>%s</sub> 
    <objs>
    <name>%s</name>
    <tag>%s</tag>
    <iden>%s</iden>
    <value>%s</value>
    <tvalue>%s</tvalue>
    </objs>
    <objs>
    <name>%s</name>
    <tag>%s</tag>
    <iden>%s</iden>
    <value>%s</value>
    <tvalue>%s</tvalue>
    </objs>
    <objs>
    <name>%s</name>
    <tag>%s</tag>
    <iden>%s</iden>
    <value>%s</value>
    <tvalue>%s</tvalue>
    </objs>
    </data>
      """
      src = """<?xml version="1.0" encoding="utf-8" ?><container>
    <filename>%s</filename>
    </container>"""
      print '[*] saving'
      f = open(self.path,'w+')
      xmlFile = minidom.parseString(src%('result.json')).firstChild
      for k,i in  enumerate(self.urls):
        elm = minidom.parseString(temple%(i,'e1','div','class','picture','.option(img=alt*src)',
                                            'e2','h1','class','page-title','.text',
                                            'e3','nav','class','woocommerce-breadcrumb',".option{.find_all('a')[2]=text*href}" )).firstChild
        print elm
        xmlFile.appendChild(elm)
      f.writelines(xmlFile.toprettyxml())
      f.close()

if __name__ == "__main__":
  try:
    print "[*] welecome to crawler"
    crow    = crawl('sm.json')
    crow.start = time()
    crow.run(raw_input() or "http://www.meublatex.com/wp-content/uploads/")
  except KeyboardInterrupt as e :
    print e
    crow.main_save()

		
	
