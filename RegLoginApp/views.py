from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from .models import *

def index(request):
    context = {
        'AllUsers': User.objects.all()
    }
    return render(request, 'index.html', context)

def register(request):
    if request.method == "POST":
        errors = User.objects.RegistrationValidator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            print(request.POST['password'])
            hashedpw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            print(hashedpw)
            newUser = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hashedpw)
            request.session['user'] = newUser.id
            return redirect("/travelers")
    else:
        return redirect('/')

def login(request):
    if request.method == "POST":
        errors = User.objects.LoginValidator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            LoggedUser = User.objects.get(email=request.POST['email'])
            request.session['user'] = LoggedUser.id
            return redirect("/travelers")
    else:
        return redirect('/')

def logout(request):
    del request.session['user']
    return redirect('/')




# Create your views here.
