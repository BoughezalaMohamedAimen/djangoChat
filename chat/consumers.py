from channels.consumer import AsyncConsumer
from django.contrib.auth.models import User
from channels.db import database_sync_to_async
from .models import Messag
import json

@database_sync_to_async
def get_user(id):
    # try:
    usr=User.objects.get(id=id)
    return usr
    # except:
    #     return 0


@database_sync_to_async
def db_save_message(senderr,reciverr,message):
    message=Messag(senderr=senderr,reciverr=reciverr,message=message)
    message.save()


class ChatConsumer(AsyncConsumer):

    async def websocket_connect(self,event):
        await self.send({
        "type": "websocket.accept"
        })
        await self.channel_layer.group_add(self.scope['user'].username, self.channel_name)



    async def websocket_receive(self,event):
        data_to_send=json.loads(event["text"])
        user_to_send= await get_user(data_to_send['username'])
        await db_save_message(senderr=self.scope['user'],reciverr=user_to_send,message=data_to_send['usermsg'])
        data_to_send['username']=self.scope['user'].username
        await self.send({
        "type": "websocket.send",
        'text': json.dumps(data_to_send)
        })



    async def websocket_disconnect(self,event):
        await self.channel_layer.group_discard(self.scope['user'].username, self.channel_name)
        print(f"Removed {self.channel_name} channel to gossip")

    async def user_gossip(self, event):
        await self.send({
        "type": "websocket.send",
        'text': event['text']
        })
