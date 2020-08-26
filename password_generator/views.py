from django.shortcuts import render

# Create your views here.

def home(request):
    context={
        'password':'pankaj'
    }
    return render(request,'password_generator/home.html',context)