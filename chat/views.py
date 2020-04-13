from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .models import Messag





class HomeChat(LoginRequiredMixin,TemplateView):
    def get(self,request):
        return render(request,'chat/home.html',{'users':User.objects.all()})





class GetDiscussion(LoginRequiredMixin,TemplateView):
    def get(self,request,usr):
        messages=Messag.objects.filter(senderr=request.user,reciverr=usr)
        return render(request,'chat/discussion.html',{'messages':messages})



class ClearMessage(LoginRequiredMixin,TemplateView):
    def get(self,request,frm):
        message=Messag.objects.filter(senderr=frm,reciverr=request.user).update(vu=True)
        return HttpResponse(status=204)
