from django.shortcuts import render
from .models import RealState
from .forms import ReserveForm

def home(request):
    realStates = RealState.objects.all()
    return render(request, 'home.html', {'realStates': realStates})


def info(request,id=0):
    realState = RealState.objects.get(pk=id)
    if request.method == "POST":
        form = ReserveForm(request.POST)
        print (realState.rents)
    else:
        form = ReserveForm()
    return render(request, 'info.html', {'realState': realState, 'form': form})
