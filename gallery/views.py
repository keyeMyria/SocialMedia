# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.conf import settings
import os

# Create your views here.

def test_1(self):
	return render(self,os.path.join("test.html",''),locals())
def serve_gallery(self):
	import os
	media_url = settings.MEDIA_URL
	
	return render(self,os.path.join("pages","gallery.html"),locals())


def serve_gallery_all(self):
	if self.user.is_authenticated():
		from .models import gallery_img 
		import json,os
		img_list=[{"img" : obj._as_dict()} for obj in gallery_img.objects.filter(user_id=self.user.id).order_by('created')]
		return HttpResponse(json.dumps({"data":img_list}),content_type='application/json')
	else:
		return HttpResponse({"data-no":"no"},content_type='application/json')