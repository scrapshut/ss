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

# import  asyncio
# import  json
# from  channels . consumer  import  AsyncConsumer
# from  channels . db  import  database_sync_to_async
# from  channels . generic . websocket  import  AsyncJsonWebsocketConsumer
# from   . models  import  Profile
# from  django . contrib . auth . models  import  User
# from  django . template . loader  import  render_to_string
#
#  class   NewUserConsumer ( AsyncJsonWebsocketConsumer ) :
# 	 async  def  connect ( self ) :
# 		 await  self . accept ( )
# 		 await  self . channel_layer . group_add ( "users" ,   self . channel_name )
#
# 		 user   =   self . scope [ 'user' ]
# 		 if   user . is_authenticated :
# 			 await  self . update_user_status ( user , True )
# 			 await  self . send_status ( )
#
# 	 async  def  disconnect ( self ,   code ) :
# 		 await  self . channel_layer . group_discard ( "users" ,   self . channel_name )
#
# 		 user   =   self . scope [ 'user' ]
# 		 if   user . is_authenticated :
# 			 await  self . update_user_status ( user , False )
# 			 await  self . send_status ( )
#
# 	 async  def  send_status ( self ) :
# 		 users   =   User . objects . all ( )
# 		 html_users   =   render_to_string ( "includes/users.html" , { 'users' : users } )
# 		 await  self . channel_layer . group_send (
# 			 'users' ,
# 			 {
# 				 "type" :   "user_update" ,
# 				 "event" :   "Change Status" ,
# 				 "html_users" :   html _ users
# 			 }
# 		 )
#
# 	 async  def  user_update ( self , event ) :
# 		 await  self . send_json ( event )
# 		 print ( 'user_update' , event )
#
# 	 @ database_sync_to_async
# 	 def  update_user_status ( self ,   user , status ) :
# 		 return   Profile . objects . filter ( user_id = user . pk ) . update ( status = status )
