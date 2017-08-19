
from django.conf import settings
import uuid as u


class save_requests(object):
	def process_request(self,req):
		req.vieww="sas"
		save=[]
		post=len(dict(req.POST.iterlists()))
		get=len(dict(req.GET.iterlists()))
		s=False
		if post > 1:
			save.append(req.POST)
			s=True
		if get > 1:
			save.append(req.GET)
			s=True
		#print help(req)#help(req)
		

		if s: #expectation for csrf
			f=open(settings.SECURITY_CHECK+"-"+str(u.uuid1())+".rq",'wb+')
			f.writelines(str(save))
			f.close()
	    	return None


		