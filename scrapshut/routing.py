from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from notifier.consumers import NewUserConsumer
from notifier.consumers import NewUserConsumer

from notifier.token_auth import TokenAuthMiddlewareStack

application = ProtocolTypeRouter({
    "websocket": TokenAuthMiddlewareStack(
        URLRouter([
            path("new/", NewUserConsumer),
        ]),
    ),

})
# application = ProtocolTypeRouter({
#     'websocket': AuthMiddlewareStack(
#     	URLRouter(
#     		[
#     			path("new/", ),
#     		]
#     	)
#     )
# })
# application = ProtocolTypeRouter({
#     'websocket':AuthMiddlewareStack(
#     	URLRouter(
#     		[
#     			path("new/", NewUserConsumer),
#                 #   path('taxi/', TaxiConsumer),
#                 # path("like/", TokenAuthMiddleware),
#
#     		]
#     	)
#     )
# })
