from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request,'home.html')

def signup(request):
 
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form=RegisterUserForm
        if request.method=='POST':
            form= RegisterUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.successs(request, 'Account was created for ' + user)
                return redirect('login')

        context= {'form': form}
        return render(request, 'signup.html' , context)

def login_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        User = authenticate(request, username=username, password=password)
        if User is not None:
            login(request, User)
            return redirect('home')
        else:
            messages.success(request, 'Wrong Username or Password. Try again.')
            return redirect('login')
    else:
        return render(request,'login.html')


def logout_user(request):
    logout(request)
    return redirect('home')