from channels.routing import route
from consumers import *



channel_routing = [
	route("websocket.connect",ws_connect),
	route("websocket.receive",ws_receive,path=r"^/ws/check_user"),
	route("websocket.receive",ws_check_friends,path=r"^/ws/chat_list"),
	route("websocket.disconnect",ws_disconnect),
]
