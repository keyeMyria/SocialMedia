from __future__ import unicode_literals

from django.db import models


from django.contrib.auth.models import User

# Create your models here.




class task_tmp(models.Model):
	id = models.IntegerField(primary_key=True)
	title = models.TextField(null=True,blank=True)
	finished = models.BooleanField(default=False)
	created_by =models.OneToOneField(User,on_delete=models.CASCADE,null=False,blank=False)
	created = models.DateTimeField(auto_now_add=True)

	

