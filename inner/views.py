from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.models import User as user
from scrp.models import user as user2
from scrp.models import poste as p
import json,os,requests

from mstf.frame import msg_maker

mimetype = 'application/json'


def test(a,b):
	try:
	  exec("""c =user.objects.filter(%s=b['name'])"""%(a))
	  return c.values()
	except Exception as e:
		return None

@csrf_exempt
def  look_for_users(self):
	p=self.POST
	d=['username','first_name','last_name','email']
	data=[]
	for i in d: 
	  a=test(i,p) 
	  if a:	
	  	for j in a: 
	  		tmp={}
	  		tmp["id"]=j["id"]
	  		tmp["username"]=j["username"]
	  		tmp["f"]=j["first_name"]+" "+j["last_name"]
	  		tmp["email"]=j["email"]
	  		tmp["img"]=im_id(long(j["id"]))
	  		data.append(tmp)
	data=json.dumps(data)
	return HttpResponse(data,mimetype)

@csrf_exempt
def pic_im1(self):
	try:
	  pk= self.POST["id"]
	except:
	  pk=self.user.id
	try:
	  exec("""data =user2.objects.filter(use_id=%s)"""%(pk))
	  return HttpResponse("/media/"+data.values()[0]["img"])
	except:
	  return HttpResponse("static/img/logo.png")	
	


@csrf_exempt
def pic_im2(self):
	try:
	  pk= self.POST["id"]
	except:
	  pk=self.user.id
	try:
	  exec("""data =user2.objects.filter(use_id=%s)"""%(pk))
	  return HttpResponse("/media/"+data.values()[0]["img_c"])
	except:
	  return HttpResponse("static/img/logo.png")	

@csrf_exempt
def im_id(ie):
	try:
	  exec("""data =user2.objects.filter(use_id=%s)"""%(ie))
	  return "media/"+str(data[0].img)
	except Exception:
		return "static/img/logo.png"

@csrf_exempt
def poste(self):
	if self.user.is_authenticated():
		try:
			po=self.POST["pp"]
			if po=="":
				return HttpResponse("are you pentesting me ! be weare of your actions ! not cool :)")
			np=p()
			np.post=po
			np.user_id=self.user.id
			np.save()
			return HttpResponse("100")
		except Exception as e:
			return HttpResponse("150")
	return HttpResponse("200")
@csrf_exempt
def load_site(self):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	try:
		url=self.POST["url"]
	except:
		return HttpResponse("100")
	#chek_url() dave or not make black liste
	try:
		res=requests.get(url, headers=headers).content
	except Exception as e:
		return HttpResponse("100 "+str(e))
	return HttpResponse("200 "+str(res))

@csrf_exempt
def status(self):
	try:
		i=int(self.POST["ic"])
		pid=int(self.POST["pid"])
		if pid==-1:
			pid=self.user.id
		msg_maker("serving  pid",str(pid))
		if self.user.is_authenticated():
			data=[]
			query=(p.objects.filter(user_id=pid).order_by("date")[::-1])[i:i+4]
			for  f in query:
				rq={}
				rq["author"]=user.objects.filter(pk=f.user_id)[0].username
				rq["post"]=f.post
				rq["userid"]=f.user_id  
				data.append(rq)
			rq=json.dumps(data)

		else:
			rq=""
	except Exception as e:
		rq=""
	return HttpResponse(rq,mimetype)
@csrf_exempt
def passcheck(self):
  try:
	if self.POST:
		t=user.objects.get(username=self.POST["user"])
		if t:
			if t.check_password(self.POST["pass"]):
				return HttpResponse("100")
			else:
				return HttpResponse("50")
  except Exception as e:
  	 return HttpResponse("5848")
