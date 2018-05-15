from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import logging,os
from django.conf import settings
debug= logging.getLogger('debug_logger').debug

# Create your models here.

class db_site(models.Model):
	Fid=models.AutoField(primary_key=True)
	Uid=models.ForeignKey(User,blank=False,null=False,on_delete=models.CASCADE,)
	mypat=models.FileField(upload_to=os.path.join(settings.BASE_DIR,'patterns')[1:],null=False,blank=False)
	base_url=models.URLField(blank=False,null=False)
	def create_patter(self,pats):
		try:
			name= self.ret_uname()+".txt"
			f= open(name,"wb+")
			if pats:
				f.writelines(pats)
			self.mypat.save(name,f)
			f.close()
		except Exception as e:
			debug(e)
			return False,e
		return True
	def ret_uname(self):
		return str(self.Uid)+'-'+str(self.Fid)+'-pattern'
