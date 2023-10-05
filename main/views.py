from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Restaurant  # Импортируем модель Restaurant

def index(request):
    return render(request, 'main/index.html')


def index2(request):
    return render(request, 'main/index2.html')



