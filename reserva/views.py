from django.shortcuts import render
from .models import RealState
from .forms import ReserveForm
from .models import RentDate
from .models import Reservation
from random import randrange
import datetime

def home(request):
    realStates = RealState.objects.all()
    return render(request, 'home.html', {'realStates': realStates})

#fechas.objects.filter(fecha ==desde, fecha == hasta, property__city == 'mdp')
##doble guion accede al atributo
def info(request,id=0):
    realState = RealState.objects.get(pk=id)
    availableDates = get_dates_available(id)
    is_reserved = False
    err = False

    #set_fechas_requeridas.add(datetime.date(2017,06,12))
    ##queremos crear dos sets, pero cambiar lel tipo de fecha a date , no datetime para que matchee cuando hagamos el issuperset

    if request.method == "POST":
        form = ReserveForm(request.POST)
        if form.is_valid():
            dateFrom = form.cleaned_data['Desde']
            dateTo = form.cleaned_data['Hasta']
            requiredDates= fechas_requeridas(dateFrom,dateTo)
            if is_available(requiredDates, availableDates):
                reser = Reservation()
                reser.name = form.cleaned_data['Nomrbre']
                reser.code = randrange(20000)
                reser.total = len(requiredDates)* (realState.price * 1.08)
                reser.save()
                for requiredDate in requiredDates:
                    print(requiredDate)
                    rentDate = RentDate.objects.filter(date=requiredDate, reservation=None)
                    rentDate.update(reservation=reser)
                availableDates = get_dates_available(id)
                form = ReserveForm()
                is_reserved = True
            else:
                err = True

    else:
        form = ReserveForm()
    
    return render(request, 'info.html', {'realState': realState, 'form': form, 'availableDates': availableDates, 'isReserved': is_reserved, 'err': err})

def is_available(requiredDates,availableDates):
    return availableDates.issuperset(requiredDates)


#recibe un id y devuelve un set de fechas(no Rentdates) disponible para esa casa
def get_dates_available(id):
    rentdates_available = RentDate.objects.filter(RealState__id=id, reservation = None)
    date_list = rentdates_available.all()
    dates_peladas = set()
    for fecha in date_list:
        dates_peladas.add(fecha.date)
    return dates_peladas

def fechas_requeridas(dateFrom, dateTo):
    fechas_usuario = set()
    delta = dateTo - dateFrom
    for i in range(delta.days+1):
        fechas_usuario.add(dateFrom)
        dateFrom += datetime.timedelta(days=1)
    return fechas_usuario

