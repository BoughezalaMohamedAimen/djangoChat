from django.shortcuts import render
from django.contrib.auth.models import User



def HomeChat(request):
    return render(request,'chat/home.html',{'users':User.objects.all()})
