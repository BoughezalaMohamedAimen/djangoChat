from django.db import models
from django.contrib.auth.models import User
from chat.models import Messag
from django.db.models.signals import post_save
from datetime import datetime

import os
import hashlib

WILAYA_CHOICES = (
('Adrar', 'Adrar'),
('Chlef', 'Chlef'),
('Laghwat', 'Laghwat'),
('Oum El Bouaghi', 'Oum El Bouaghi'),
('Batna', 'Batna'),
('Bejaya', 'Bejaya'),
('Biskra', 'Biskra'),
('Bechar', 'Bechar'),
('Blida', 'Blida'),
('Bouira', 'Bouira'),
('Tamanrasset', 'Tamanrasset'),
('Tebessa', 'Tebessa'),
('Telecmcen', 'Telecmcen'),
('Tiaret', 'Tiaret'),
('Tizi Ouzou', 'Tizi Ouzou'),
('Alger', 'Alger'),
('Djelfa', 'Djelfa'),
('Jijel', 'Jijel'),
('Sétif', 'Sétif'),
('Saida', 'Saida'),
('Skikda', 'Skikda'),
('Sidi Bel Abbès', 'Sidi Bel Abbès'),
('Annaba', 'Annaba'),
('Guelma', 'Guelma'),
('Constantine', 'Constantine'),
('Médéa', 'Médéa'),
('Mostaganem', 'Mostaganem'),
('Msila', 'M\'Sila'),
('Mascara', 'Mascara'),
('Ouargla', 'Ouargla'),
('Oran', 'Oran'),
('El Bayadh', 'El Bayadh'),
('Illizi', 'Illizi'),
('Bordj Bou Arreridj', 'Bordj Bou Arreridj'),
('Boumerdès', 'Boumerdès'),
('El Tarf', 'El Tarf'),
('Tindouf', 'Tindouf'),
('Tissemsilt', 'Tissemsilt'),
('El Oued', 'El Oued'),
('Khenchela', 'Khenchela'),
('Souk Ahras', 'Souk Ahras'),
('Tipaza', 'Tipaza'),
('Mila', 'Mila'),
('Aïn Defla', 'Aïn Defla'),
('Naâma', 'Naâma'),
('Témouchent', 'Témouchent'),
('Ghardaïa', 'Ghardaïa'),
('Relizane', 'Relizane'),
            )


def createactive():
    return hashlib.md5(str(datetime.now()).encode()).hexdigest()


# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null='True')
    wilaya=models.CharField(null='True',max_length=255,choices=WILAYA_CHOICES)
    ville=models.CharField(null='True',max_length=255)
    adresse=models.CharField(null='True',max_length=255)
    telephone=models.CharField(null='True',max_length=10)
    activate=models.CharField(max_length=255,unique='True')

    def __str__(self):
        return self.user.username

    def count_unread(self,senderr):
        msglen=len(Messag.objects.filter(reciverr=self.user,senderr=senderr,vu=False))
        print(f"sender {senderr }**************** {msglen}   reciver {self.user }*")
        return msglen




def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'],activate=createactive())

post_save.connect(create_profile, sender=User)
