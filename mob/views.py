from django.shortcuts import render
from os import listdir
from django.http import HttpResponse
from django.utils.encoding import smart_str
import logging,json,os
from .models import task_tmp as at
# Create your views here.
debug= logging.getLogger('debug_logger').debug



def download(self):
	return render(self,os.path.join("pages","mobile_serve.html"))	
def download_list(self):
	try:
		direc = self.POST["direc"]
	except Exception as e:
		direc = "/home/med/Downloads/"
		debug(e)	
	jdata = {}
	data = listdir(direc)
	for k,i in enumerate(data):
		jdata[k]=os.path.join(direc,i)
	return HttpResponse(json.dumps(jdata),"json/application")

def download_file(self):
	try:
		filep = self.GET['path']
	except Exception as e:
		debug(e)
		filep = "/home/med/Downloads/Myrath - Legacy (Full Album).mp3"
	response = HttpResponse(open(filep,'r').read(),content_type="application/force-download")
	response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filep.split('/')[-1].replace(" ",''))
	debug(filep.split('/')[-1])
	return response



def listen_updates(self):
	tasks = at.objects.filter(finished=False)
	for i in range(len(tasks)):
		data[i]=tasks[i]

	return HttpResponse(json.dumps(data),"json/application")