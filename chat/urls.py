from django.contrib import admin
from django.urls import path,include,re_path
from .views import *


urlpatterns = [
        re_path(r'^$',HomeChat.as_view(),name='HomeChat'),
        path('discussion/<int:usr>', GetDiscussion.as_view(),name='GetDiscussion'),
        path('clear/message/<int:frm>', ClearMessage.as_view(),name='ClearMessage'),

]
