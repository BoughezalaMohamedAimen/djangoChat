from django.db import models
from django.contrib.auth.models import User


class Messag(models.Model):
    heure=models.DateTimeField(auto_now_add=True)
    senderr=models.ForeignKey(User,on_delete=models.CASCADE,related_name="message_from")
    reciverr=models.ForeignKey(User,on_delete=models.CASCADE,related_name="message_to")
    message=models.CharField(max_length=255)
    vu=models.BooleanField(default=False)

    def message_from(self):
        return self.senderr

    def message_to(self):
        return self.reciverr

    def __str__(self):
        return f"at: {self.heure} from {self.senderr.username} to {self.reciverr.username} body: {self.message} "



from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import json

@receiver(post_save, sender=Messag)
def achat_item_handler(sender, **kwargs):
    to_send=json.dumps({
    'username':kwargs['instance'].senderr.username,
    'usermsg':kwargs['instance'].message,
    'userid':kwargs['instance'].senderr.id,
    })
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
            kwargs['instance'].reciverr.username, {"type": "user.gossip",
                       "event": "New Message",
                       "text":to_send})
