from channels.generic.websocket import AsyncJsonWebsocketConsumer

class NewUserConsumer(AsyncJsonWebsocketConsumer):
	async def connect(self):
		print('connect')
		await self.accept()
		await self.channel_layer.group_add("users", self.channel_name)
		print(f"Add {self.channel_name} channel to users's group")

	async def receive_json(self, message):
		print("receive",message)
		
	async def disconnect(self, close_code):
		await self.channel_layer.group_discard("users", self.channel_name)
		print(f"Remove {self.channel_name} channel from users's group")

	async def user_update(self,event):
		await self.send_json(event)
		print('user updated',event)