# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class gallery_img(models.Model):
	img     = models.ImageField(upload_to='gallery_img')
	created = models.DateTimeField(auto_now_add=True)
	user_id = models.IntegerField()
	def _as_dict(self):
		return {'img':str(self.img)}

	class Meta:
		app_label = 'gallery'
	