from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import UserLoginForm


def user_login(request):
    if request.method == 'POST'
