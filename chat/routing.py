from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from .consumers import ChatConsumer


application = ProtocolTypeRouter({
"websocket":AuthMiddlewareStack(
URLRouter([
path('chat/ws/',ChatConsumer)
])
)

})
