from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import *


class RegistrationForm(UserCreationForm):
    email=forms.EmailField( required='True');
    is_active=False

    class Meta:
        model=User
        fields=['email','username','password1','password2','first_name','last_name','is_active']

class EditProfileForm(forms.ModelForm):
    prefix='profile'
    maps=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'2'}),required=False)
    class Meta:
        model=UserProfile
        exclude=['activate',]

class EditUserForm(UserChangeForm):
    prefix='user'
    class Meta:
        model=User
        fields=['first_name','last_name','email',]

class activateAccountForm(forms.Form):
    email=forms.EmailField( required='True');


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





class AccountFilter(forms.Form):
    wilaya=forms.CharField(widget=forms.Select(choices =WILAYA_CHOICES,
    attrs={
    'class': 'selectpicker form-control bg-white border filterr',
    'multiple':'',
    'data-live-search':'true',
    'title':'Wilaya'
    }),required=False)
    mot_cle=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control filterr'}),required=False)
