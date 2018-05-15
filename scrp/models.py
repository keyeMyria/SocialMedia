from __future__ import unicode_literals

from django.db import models
from captcha.fields import CaptchaField
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import os
from itertools import chain
from django.utils.timezone import now 
# Create your models here.

class user(models.Model):
	use=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
	img=models.ImageField(upload_to="static/img/",null=True)
	img_c=models.ImageField(upload_to="static/img/",null=True)
	#about
	work = models.CharField(max_length=30,null=True)
	hometown = models.CharField(max_length=30,null=True)
	current_town = models.CharField(max_length=30,null=True)
	birth_date = models.DateTimeField(default=now,null=True)
	
	#relation_with


	#_ids=models.CharField(max_length=30,null=True)
	 	



class site(models.Model):
	_id=models.AutoField(primary_key=True,null=False,default=0)
	id=models.ForeignKey('user',null=False,on_delete=models.CASCADE,)
	require=models.BooleanField()
	user_pass=models.CharField(max_length=350)






class Post_Manager(models.Manager):
	def get_postes(self,tid):
		req1 = super().get_queryset().filter(postFrom=tid)
		req2 = super().get_queryset().filter(postTo=tid)

		return req2 | req1





class poste(models.Model):
	postFrom = models.ForeignKey(User,null=True,related_name='sender',on_delete=models.CASCADE,)
	postTo = models.ForeignKey(User,null=True,related_name='receiver',on_delete=models.CASCADE,)
	date  = models.DateTimeField(auto_now_add=True)
	postID =models.AutoField(primary_key=True,blank=False)
	poste=models.TextField(blank=False,null=False)
	objects = models.Manager() 
	p_mngr = Post_Manager() 
	class Meta:
		app_label='scrp'





		

#class captch(models.Model):
#	captcha = CaptchaField()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user.objects.create(use=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.user.save()
