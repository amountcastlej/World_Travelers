from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import * 
from RegLoginApp.models import User

def travelersIndex(request):
    context = {
        'user': User.objects.get(id=request.session['user']),
        'allTrips': Trip.objects.all()
    }
    return render(request, 'travelers.html', context)

def addTrip(request):
    LoggedUser = User.objects.get(id=request.session['user'])
    newTrip = Trip.objects.create(location=request.POST['location'], date=request.POST['date'], traveler=LoggedUser)
    print(newTrip.location)
    return redirect('/travelers')
