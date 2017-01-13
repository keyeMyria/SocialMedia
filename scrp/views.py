from django.shortcuts import render
from .forms import CaptchaTestForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User as user
from django.conf import settings
import sqlite3 as sq


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


def main(self):
	if self.user.is_authenticated():
			title='welecome home  %s '%(self.user)

	return render(self,"pages/home.html")

def sign(self):
	form=user(self.POST or None)
	form_c = CaptchaTestForm(self.POST or None)

	if self.POST:	
		if form.is_valid() and form_c.is_valid():
			instance=form.save(commit=False)
			instance.save()
			return render(self,"pages/sign_done.html",locals())

	return render(self,"pages/sign in.html",locals())
@csrf_exempt
def pattern(self):
	print "reached self" ,self.POST
	#if self.user.is_authenticated():
	if self.POST:
		pat=self.POST["pat"]
		user= connnect()
		user=user.find_user("id =1 ")
		return HttpResponse(user)	

	else:
		return redirect("/")
def prof(self):
  try:
  		direc=self.GET["id"]
		title=get_object_or_404(user,pk=direc).username
		return render(self,"registration/profile.html",locals())
  except:
	if self.user.is_authenticated():
		#im1=get_object_or_404(user,pk=self.user.id)
		title=self.user
		direc=self.user.id
		return render(self,"registration/profile.html",locals())
	else:
		return redirect('/accounts/login/')