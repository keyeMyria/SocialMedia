from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ChatMessage(models.Model):
	sender   = models.ForeignKey(User, related_name = 'sender_user')
	receiver = models.ForeignKey(User, related_name = 'receiver_user')
	message  = models.CharField(max_length = 200)
	received_at = models.DateTimeField(auto_now_add = True)
	read_on = models.DateTimeField()
	is_read = models.BooleanField(default=False)
	new = models.BooleanField(default=True)
	def json_pack(self):
		return {"sender":self.sender.id,"receiver":self.receiver.id,
				"message":self.message,"is_read":self.is_read,
				"read_on":str(self.read_on)}