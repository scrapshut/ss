import asyncio
import json
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
# from .models import Post
from django.contrib.auth.models import User
from django.template.loader import render_to_string

class NewUserConsumer(AsyncJsonWebsocketConsumer):
	def receive(self, text_data=None, bytes_data=None):
	    if self.scope['user'].id:
	        pass
	    else:
	        try:
	            # It means user is not authenticated yet.
	            data = json.loads(text_data)
	            if 'token' in data.keys():
	                token = data['token']
	                user = fetch_user_from_token(token)
	                self.scope['user'] = user

	        except Exception as e:
	            # Data is not valid, so close it.
	            print(e)
	            pass

	    if not self.scope['user'].id:
	        self.close()
	async def connect(self):
		user = self.scope['user']
		if user.is_authenticated:
			await self.accept()
			await self.channel_layer.group_add("users", self.channel_name)
		else:
			print("unauthenticated")


	async def disconnect(self, code):
		await self.channel_layer.group_discard("users", self.channel_name)
