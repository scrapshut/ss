from channels.auth import AuthMiddlewareStack
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import User
# user=get_user_model
from django.contrib.auth import get_user_model
User = get_user_model()

# def get(request):
#     for user in User.objects.all():
#         token=Token.objects.get_or_create(user=request.user)
#         if token.user:
#             print("ok")
#         else:
#             print("not okay")
#         print(token)


class TokenAuthMiddleware:
    """
    Token authorization middleware for Django Channels 2
    """
    # def get(request):
    #     for user in User.objects.all():
    #         token=Token.objects.get_or_create(user=request.user)
    #         print(token)
    def get(request):
        for user in User.objects.all():
            token=Token.objects.get_or_create(user=request.user)
            if token.user:
                print("ok")
            else:
                print("not okay")
            print(token)
    def __init__(self, inner):
        self.inner = inner

    def __call__(self,scope):
        # headers = dict(scope['headers'])
        # if b'authorization' in headers:
        #     try:
        #         token_name, token_key = headers[b'authorization'].decode().split()
        #         if token_name == 'Token':
        # token=Token.objects.get_or_create(user=user)
        # print(token)

        token = Token.objects.get(key='175f76fd9b63a9477bf5f9a6f2e9a7f12ac62d65')
        if token.user:
            scope['user'] = token.user
        else:
            scope['user'] = AnonymousUser()
        return self.inner(scope)

TokenAuthMiddlewareStack = lambda inner: TokenAuthMiddleware(AuthMiddlewareStack(inner))
# class TokenAuthMiddleware:
#     """
#     Token authorization middleware for Django Channels 2
#     """
#
#     def __init__(self, inner):
#         self.inner = inner
#
#     def __call__(self, scope):
#         headers = dict(scope['headers'])
#         if b'authorization' in headers:
#             try:
#                 token_name, token_key = headers[b'authorization'].decode().split()
#                 if token_name == 'Token':
#                     token = Token.objects.get(key=token_key)
#                     scope['user'] = token.user
#             except Token.DoesNotExist:
#                 scope['user'] = AnonymousUser()
#         return self.inner(scope)
#
# TokenAuthMiddlewareStack = lambda inner: TokenAuthMiddleware(AuthMiddlewareStack(inner))
