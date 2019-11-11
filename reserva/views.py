from django.shortcuts import render
from .models import RealState

def home(request):
    realStates = RealState.objects.all()
    return render(request, 'home.html', {'realStates': realStates})

def info(request,id=0):
    realState = RealState.objects.get(pk=id)
    return render(request, 'info.html', {'realState': realState})
