from django.shortcuts import render
from .models import RealState

def home(request):
    realStates = RealState.objects.all()
    return render(request, 'home.html', {'realStates': realStates})