from django.shortcuts import render, redirect
from django.http import HttpResponse 

def index(request):
    return render(request, "base.html")

def account_no(request):
    return render(request, "account_no.html")

def video(request):
    return render(request, "video.html")

def profile(request):
    return render(request, "profile.html")

def transfer_money(request):
    return render(request, "transfer_money.html")
