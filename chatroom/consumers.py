from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http
from models import *
import json

@channel_session_user_from_http
def ws_connect(msg):
	msg.reply_channel.send({"text":"connected"})


@channel_session_user
def ws_receive(msg):
	print msg.user.id
	data=[]
	for i in  ChatMessage.objects.filter(receiver=msg.user.id,new=True):
		data.append(i.json_pack())
	if data:
		msg.reply_channel.send({"text":json.dumps(data)})





@channel_session_user
def ws_disconnect(msg):
	pass

