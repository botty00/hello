"""quiz3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("hello",views.hello,name="hello"),
    path('create_user',views.create_user,name='create_user'),
    path('loginview',views.loginview,name='loginview'),
    path('question1',views.question1,name='question1'),
    path('question2',views.question2,name='question2'),
    path('question3',views.question3,name='question3'),
    path('answer/<int:correct>',views.answer,name='answer'),
    path('answer2/<int:correct>',views.answer2,name='answer2'),
    path('answer3/<int:correct>',views.answer3,name='answer3'),
    path('result',views.result,name='result'),
    path('start',views.start,name='start'),
    path('top',views.top,name='top'),
    path('complete',views.complete,name='complete'),
    path('logoutview',views.logoutview,name='logoutview'),
]
