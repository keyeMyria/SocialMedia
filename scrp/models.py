from __future__ import unicode_literals

from django.db import models
from captcha.fields import CaptchaField
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import os,datetime
# Create your models here.

class user(models.Model):
	use=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
	img=models.ImageField(upload_to="static/img/",null=True)
	img_c=models.ImageField(upload_to="static/img/",null=True)
	_ids=models.CharField(max_length=30,null=True)
	 	



class site(models.Model):
	_id=models.AutoField(primary_key=True,null=False,default=0)
	id=models.ForeignKey('user',null=False)
	require=models.BooleanField()
	user_pass=models.CharField(max_length=350)
	pat=models.FileField(upload_to=os.path.join(settings.BASE_DIR,'patterns'))



class poste(models.Model):
	date = models.DateTimeField(primary_key=True,auto_now_add=True,auto_now=False, blank=True)
	user_id=models.IntegerField(blank=False)
	post=models.TextField(blank=False,null=False)
	class Meta:
		app_label='scrp'
		
#class captch(models.Model):
#	captcha = CaptchaField()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
    	print instance
        user.objects.create(use=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.user.save()