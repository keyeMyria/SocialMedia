from django.shortcuts import render
from .forms import CaptchaTestForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User as user
from django.conf import settings
import sqlite3 as sq
import os,logging




class connnect(object):
	def __init__(self):
		self.con=sq.connect(settings.DATABASES["default"]["NAME"])
		self.c=self.con.cursor()
	def find_user(self,cond):
		if cond is None:
			cond="1=1"
		self.c.execute("SELECT * FROM table_user where  %s  "%(cond))
		self.c.commit()
		return self.c.fetchall()




# Create your views here.
debug= logging.getLogger('debug_logger').debug


def main(self):

	if self.user.is_authenticated:
			title='welecome home  %s '%(self.user.first_name)
			return render(self,"pages/home.html",locals())
	else:
			return redirect("/accounts/login/")

def setup(self):

	try:
		p=self.POST["pass"]
	except :
		p=None

	try:
		f=self.POST["first"]
	except :
		f=None
	try:
		l=self.POST["last"] 
	except :
		l=None
	print(self.POST)
				
	if self.user.is_authenticated():
		title = 'setting up profile'
		if p or l or f:
			u=user.objects.get(pk=self.user.id)
			if control(p,'pass') and p :
				u.set_password(p)
			if control(f, 'name') and f:
				u.first_name=f
			if control(l, 'name') and l:
				u.last_name=l
			u.save()
			return HttpResponse("200")
		else:
			return render(self, os.path.join("pages","settings.html"),locals())

			
	else:
		redirect("/")

def sign(self):
	form=user(self.POST or None)
	form_c = CaptchaTestForm(self.POST or None)

	if self.POST:	
		if form.is_valid() and form_c.is_valid():
			instance=form.save(commit=False)
			instance.save()
			return render(self,os.path.join("pages","sign in.html"),locals())

	return render(self,os.path.join("pages","sign in.html"),locals())
@csrf_exempt
def pattern(self):
	#if self.user.is_authenticated():
	if self.POST:
		pat=self.POST["pat"]
		user= connnect()
		user=user.find_user("id =1 ")
		return HttpResponse(user)	

	else:
		return redirect("/")

def prof(self):
	if self.user.is_authenticated:

		direc = self.user.id 
		title = self.user.get_full_name() or "Unknow user name"
		return render(self,os.path.join("registration","profile.html"),locals())
	else:
		return redirect('/accounts/login/')

def control(elem,typ):
	import string
	if elem ==None:
		return False
	if type=="user":
		pass
	if typ=="name":
		if len(elem) <=1 :
			return False
		for i in list(elem):
			if not(i in string.printable[:62]):
				return False
	elif typ=='pass':
		if len(elem)<8:
			return False

	return True
	



def  test_geio(self):
	a=str(self.META('geoip_city'))
	return HttpResponse(str(a))