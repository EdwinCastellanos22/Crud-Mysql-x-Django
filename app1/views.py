from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    dato= Usuario.objects.all()
    return render(request, 'index.html',
    {"dato":dato})
