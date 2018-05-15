# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User


class friend_request(models.Model):
	sender   = models.ForeignKey(User, related_name = 'sender_user_request',on_delete=models.CASCADE,)
	receiver = models.ForeignKey(User, related_name = 'receiver_user_request',on_delete=models.CASCADE,)
	received_at = models.DateTimeField(auto_now_add = True)
	new = models.BooleanField(default=True)
	def _accept(self):
		a = friend_bond()
		a.sender = self.sender
		a.receiver = self.receiver
		a.save()
		self.delete()		

	def _reject(self):
		self.delete()


class friend_bond(models.Model):
	sender   = models.ForeignKey(User, related_name = 'sender_user_request_hasbaccepted',on_delete=models.CASCADE,)
	receiver = models.ForeignKey(User, related_name = 'receiver_user_request_hasaccepted',on_delete=models.CASCADE,)
	received_at = models.DateTimeField(auto_now_add = True)
	new = models.BooleanField(default=True)



