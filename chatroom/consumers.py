from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http
from models import *
from friends.views import *
from friends.models import friend_bond
import json,logging

debug= logging.getLogger('debug_logger').debug

rtxt = lambda x: {"text":json.dumps(x)}

def check_sess(msg):
    if not msg.user.id:
		msg.reply_channel.send({"accept": False})
		raise  AssertionError

def add_user_ws(frome,to):
	try:
		a = friend_request.objects.get(sender_id=frome,receiver_id=to)
		a.delete()
		return "deleted"
	except:
		a = friend_request(sender_id=frome,receiver_id=to)
		a.save()
		return "sent"


def chech_user_ws(msg,f):
	resp = {}
	for i in  f.keys():
		c=int(f[i])
		if msg.user.id != c:
			resp[i]=r_friends(msg.user.id,c)[0]
	msg.reply_channel.send({"text":json.dumps(resp)})


@channel_session_user_from_http
def ws_connect(msg):
    check_sess(msg)
    msg.reply_channel.send({"accept": True})


@channel_session_user
def ws_receive(msg):	
    try:
        f= json.loads(msg.content["text"])
        if f["job"]=="check":
		    chech_user_ws(msg, f)
        elif f["job"]=="add":
            resp = add_user_ws(msg.user.id,f["to"])
            msg.reply_channel.send({"text":resp})
    except:
		pass

@channel_session_user
def ws_check_friends(msg):
	_id= msg.user.id
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
	msg.reply_channel.send(rtxt(data))

	
"""	print msg.user.id
	data=[]
	for i in  ChatMessage.objects.filter(receiver=msg.user.id,new=True):
		data.append(i.json_pack())
	if data:
		msg.reply_channel.send({"text":json.dumps(data)})
"""




@channel_session_user
def ws_disconnect(msg):
	pass

