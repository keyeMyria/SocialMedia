from django.urls import path

from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from ws.views import ws_chat,ws_check_friends



application = ProtocolTypeRouter({

    # add users and sessions - see http://channels.readthedocs.io/en/latest/topics/authentication.html
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/check_user",ws_chat ),
            path("ws/chat_list",ws_check_friends),
        ]),
    ),

})