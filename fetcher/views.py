from django.shortcuts import render
from django.contrib.auth.models import User
from .models import db_site as site
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from celery.decorators import task
import logging,os,json

debug= logging.getLogger('debug_logger').debug


# Create your views here.
@login_required
def index_pattern(self):
	return render(self, "pages/_index_pattern.html",locals())



@login_required
@csrf_exempt
def ini_Pattern(self):
	try:
		pattern =  ";@".join([self.POST["iden"],
					self.POST["ival"],
					self.POST["rad"],
					self.POST["look"],
					self.POST["get"]])
		base_url = self.POST["url"]
	except Exception as e:
		debug(e)
		return HttpResponse("missing")

	a = site.objects.create(Uid_id=User.objects.all()[0].id,base_url=base_url)
	if a.create_patter(pattern):
		a.save()
		Main_Task.delay(base_url,pattern,a.ret_uname())
		return HttpResponse('sucess')
	else:
		return HttpResponse('failed')

def check_result(self):
	try:
		number = self.POST["number"]
	except:
		return HttpResponse("n'existe pas !")
	try:
		si=site.objects.filter(Uid_id=self.user.id).reverse()[0]
	except:
		return HttpResponse("n'existe pas !")
	f=open(os.path.join(settings.R_FOLDER,si.ret_uname()+".json"))
	data=f.readlines()
	f.close()
	return HttpResponse(data,"json/application")

@task(name="scrawl_pages_for_urls")
def Main_Task(url,pat,file_name):
	import time
	from crowlp import crawl
	if pat.split(';@')[2]=="all":
		craw=crawl()
		craw.run(url,50)
		result =craw.main_ret()
		f=open(os.path.join(settings.R_FOLDER,file_name+".json"),'wb+')
		json.dump(result,f)
		f.close()
	else:
		pass

	
