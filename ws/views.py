from django.shortcuts import render

from channels.generic.websocket import AsyncJsonWebsocketConsumer


from friends.views import *

from friends.models import friend_bond


import json,logging

debug= logging.getLogger('debug_logger').debug
rtxt = lambda x: {"text":json.dumps(x)}




class ws_chat(AsyncJsonWebsocketConsumer):

	async def connect(self):
		if self.scope['user'].is_anonymous:
			await self.close()
		else:
			await self.accept()
	async def disconnect(self,code):
		pass

	async def receive_json(self,msg):
		try:
			f= json.loads(msg["text"])
			if f["job"]=="check":
				chech_user_ws(self,msg, f)
			elif f["job"]=="add":
				resp = add_user_ws(msg.user.id,f["to"])
				print(resp)
				self.send_json({"text":resp})
		except:
			pass

	async def add_user_ws(frome,to):
		try:
			a = friend_request.objects.get(sender_id=frome,receiver_id=to)
			a.delete()
			return "deleted"
		except:
			a = friend_request(sender_id=frome,receiver_id=to)
			a.save()
			return "sent"


	async def chech_user_ws(self,msg,f):
		resp = {}
		for i in  f.keys():
			c=int(f[i])
			if msg.user.id != c:
				resp[i]=r_friends(msg.user.id,c)[0]
		self.send_json({"text":json.dumps(resp)})









class ws_check_friends(AsyncJsonWebsocketConsumer):
	async def connect(self):
		if self.scope['user'].is_anonymous:
			await self.close()
		else:
			await self.accept()
	
	async def disconnect(self,code):
		pass


	async def receive_json(self,msg):
		_id= self.scope['user'].id
		a,b = friend_bond.objects.filter(sender_id=_id),friend_bond.objects.filter(receiver_id=_id)
		#create new filter to make the code more functional ***
		data=[]
		for i in a :
			if i.receiver.is_active:
				data.append({"id":i.receiver_id,"is_active":i.receiver.is_active,"name":b[0].receiver.get_full_name()})
		for i in b :
			if i.sender.is_active:
				data.append({"id":i.sender_id,"is_active":i.sender.is_active,"name":b[0].sender.get_full_name()})
		#just for testing
		#if len(a)>0:
		#	data.append({"id":a[0].receiver_id,"is_active":True,"name":b[0].receiver.get_full_name()})
		#if len(b)>0:
		#	data.append({"id":b[0].sender_id,"is_active":True,"name":b[0].sender.get_full_name()})

	#	if len(data)< 10:
			#filter 8 non connected friends and add them as non connected !
		if len(data)!=0:
			await self.send_json(rtxt(data))

