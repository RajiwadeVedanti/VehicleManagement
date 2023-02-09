from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request,"login.html")

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, "|", password)
        user = authenticate(request,username=username,password=password)
        if user:
            request.session["username"] = username
            request.session["is_staff"] = user.is_staff
            request.session["is_superuser"] = user.is_supeeruser

            return redirect("get_user")
        else:                
            return render(request,"login_response.html" ,{"response":"Login Failed!"})
     

def get_user(request):  
    print(request.session.get("username"))
    users = User.objects.all()
    return render(request,"user.html",{"users_list":users,"requested_user":request.user})

def add_user(request):
    return render(request,"add_user.html")

@csrf_exempt
def create_user(request):
    if request.method == "POST":
        request_by_user = request.user
        if request_by_user.is_authenticated and request_by_user.is_superuser:
            post_data = request.POST
            username = post_data.get("username")
            email = post_data.get("email")
            password = post_data.get("password")

            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()
            return redirect("get_user")
        else:
            return render(request,"login_response.html" ,{"response":"You cannot perform this operation!"})
    else:
        return render(request,"login_response.html" ,{"response":"Get method not allowed!"})
    
