from django.http import HttpRespesponse
from django.shortcuts import render

def home(request):
    return render(request,'base.html')