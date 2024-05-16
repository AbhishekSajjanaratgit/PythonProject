from django.http import request
from django.shortcuts import render
import pyjokes

def baseFunction(request):
    data = {"jokes":pyjokes.get_joke(category='all')}
    return render(request,"base\index.html",data)