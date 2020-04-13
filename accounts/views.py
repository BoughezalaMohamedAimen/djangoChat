from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from .forms import *
import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.

class HomeAccount(LoginRequiredMixin,TemplateView):
    def get(self,request):
        return render(request,'accounts/profile.html')

class Login(TemplateView):
    def get(self,request):
        return render(request,'accounts/login.html')

class Register(TemplateView):
    def get(self,request):
        form=RegistrationForm()
        return render(request,'accounts/register.html',{'form':form})
    def post(self,request):
            form=RegistrationForm(request.POST or None)
            if form.is_valid():
                form.save()
                user=User.objects.get(email=form.cleaned_data['email'])
                account=UserProfile.objects.get(user=user)
                send_mail('activation du compte','/account/activate/'+user.username+'/'+account.activate,'aaaa@mailmail.com',[user.email])

                return redirect('login')
            else:
                return render(request,'accounts/register.html',{'form':form})

class Profile(LoginRequiredMixin,TemplateView):
    def get(self,request):
        return render (request,'accounts/profile.html')


class OtherProfile(TemplateView):
    def get(self,request,username):
        user=User.objects.get(username=username)
        return render (request,'accounts/other_profile.html',{'profile':user})


class EditProfile(LoginRequiredMixin,TemplateView):
    def get(self,request):
        form=EditProfileForm(instance=request.user.userprofile)
        userForm=EditUserForm(instance=request.user)
        return render (request,'accounts/edit_profile.html',{'form':form,'userForm':userForm})
    def post(self,request):
        postt = request.POST.copy()
        postt.update({ 'profile-user': request.user.id })
        form=EditProfileForm(postt, request.FILES, prefix='profile',instance=request.user.userprofile)
        userForm=EditUserForm(request.POST,prefix='user',instance=request.user)

        if userForm.is_valid():
            print('saved')
            userForm.save()
        else:
            return render (request,'accounts/edit_profile.html',{'form':form,'userForm':userForm})

        if form.is_valid():
            print('saved')
            form.save()
            return redirect('profile')
        else:
            return render (request,'accounts/edit_profile.html',{'form':form,'userForm':userForm,'message':'profile'})



class ChangePassword(LoginRequiredMixin,TemplateView):
    def get(self,request):
        form=PasswordChangeForm(user=request.user)
        return render (request,'accounts/change_password.html',{'form':form})
    def post(self,request):
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            return render (request,'accounts/change_password.html',{'form':form})


def  ActivateAccount(request,username,activate):
    user=User.objects.get(username=username)
    account=UserProfile.objects.get(user=user)
    if activate==account.activate:
        user.is_active=True
        user.save()
        return redirect('login')
    else:
        return redirect('activate_account')

class ActivateAccountForm(TemplateView):
    def get(self,request):
        form=activateAccountForm()
        return render (request,'accounts/activate_account_form.html',{'form':form})
    def post(self,request):
        form=activateAccountForm(request.POST or None)
        if form.is_valid():
            try:
                user=User.objects.get(email=form.cleaned_data['email'])
                account=UserProfile.objects.get(user=user)
                send_mail('activation du compte','/account/activate/'+user.username+'/'+account.activate,'aaaa@mailmail.com',[user.email])
                return render(request,'accounts/activate_account_form.html',{'message':'un e-mail de confirmation e bien été envoyé'})
            except User.DoesNotExist:
                return render (request,'accounts/activate_account_form.html',{'form':form})

        return render (request,'accounts/activate_account_form.html',{'form':form})


class AccountList(TemplateView):
    def get(self,request):
        filter_data={}

        if request.GET.get('wilaya'):
            filter_data['wilaya__in']=request.GET.get('wilaya').split(',')


        q = Q()
        if request.GET.get('mot_cle'):
            for mot_cle in request.GET.get('mot_cle').split(','):
                q |= Q(user__username__contains=mot_cle)


        if q:
            profiles_list=UserProfile.objects.all().filter(**filter_data).filter(q)
        else:
            profiles_list=UserProfile.objects.all().filter(**filter_data)
        paginator = Paginator(profiles_list, 12) # Show 25 contacts per page

        page = request.GET.get('page')
        profiles = paginator.get_page(page)
        search=AccountFilter()
        return render(request,'accounts/accounts_list.html', {'profiles':profiles,'profiles_all_count':profiles_list.count(),'search':search})
