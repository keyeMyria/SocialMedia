from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.models import User as user
from scrp.models import user as user2
from scrp.models import poste as p
import json,os,requests, datetime

from mstf.frame import msg_maker

mimetype_json = 'application/json'


def test(a,b):
	try:
	  exec("""c =user.objects.filter(%s=b['name'])"""%(a))
	  return c.values()
	except Exception as e:
		return None


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
	return HttpResponse(data,mimetype_json)


def pic_im1(self):
	try:
	  pk= self.POST["id"]
	except:
	  pk=self.user.id
	try:
	  data =user2.objects.filter(use_id=pk)
	  return HttpResponse("/media/"+data.values()[0]["img"])
	except Exception as e:
	  return HttpResponse("static/img/logo.png")	
	



def pic_im2(self):
	try:
	  pk= self.POST["id"]
	except:
	  pk=self.user.id
	try:
	  data =user2.objects.filter(use_id=pk)
	  return HttpResponse("/media/"+data.values()[0]["img_c"])
	except:
	  return HttpResponse("static/img/logo.png")	


def im_id(ie):
	try:
	  data =user2.objects.filter(use_id=ie)
	  return "media/"+str(data[0].img)
	except Exception:
		return "static/img/logo.png"

def poste(self):
	if self.user.is_authenticated:
		try:
			po=self.POST["pp"]
			sender = self.user
			PTO = int(self.POST["PTO"])
			if po=="":
				return HttpResponse("are you pentesting me ! be weare of your actions ! not cool :/")
			np=p()
			np.poste = po
			np.postFrom = sender
			np.postTo = user.objects.get(id=PTO)
			np.save()
			return HttpResponse("100")
		except Exception as e:
			print(e)
			return HttpResponse("150")
	return HttpResponse("200")

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
#you need to add authentication for permission

def status(self):
	try:
		i=int(self.POST["ic"])
		pid=int(self.POST["pid"])
		if pid<=-1:
			pid=self.user.id
		if self.user.is_authenticated:
			data=[]
			query=(p.p_mngr.get_postes(pid)).order_by("date")[::-1][i:i+4]
			for  f in query:
				t=user.objects.filter(pk=f.postFrom.id)[0]
				rq={}
				rq["author"]=t.first_name + " " + t.last_name
				rq["post"]=f.poste
				rq["userid"]=f.postFrom.id
				data.append(rq)
			rq=json.dumps(data)

		else:
			rq=""
	except Exception as e:
		rq=""
		print("[**************]",e)
	return HttpResponse(rq,mimetype_json)




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



def pic(self):
	try:
	    img = self.FILES['file']
	    from gallery.models import gallery_img 
	    d=user2.objects.get(use=self.user.id)
	    d.img = img
	    d.save()
	    d=gallery_img.objects.create(user_id=self.user.id,img=img)
	    d.save()
	    return HttpResponse("200")
	except Exception as e:
	    print(e)
	    return HttpResponse("null")
