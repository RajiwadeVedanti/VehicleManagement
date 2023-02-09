from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate

template_path = "user/"

def home(request):
    return render(request, "login.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request,username=username,password=password)

        if user:
            request.session["username"] = username
            request.session["is_staff"] = user.is_staff
            request.session["is_superuser"] = user.is_superuser

            return redirect("get_user")
        else:                
            return render(request,"login_response.html" ,{"response":"Login Failed!"})
    else:
        return redirect("home")


def logout_user(request):
    if request.session.has_key("username"):
        del request.session["username"]
        del request.session["is_staff"]
        del request.session["is_superuser"]
    else:
        pass
    return redirect("home")

def get_user(request): 
    if request.session.has_key("username"):
        username = request.session["username"]
        is_staff = request.session["is_staff"]
        is_superuser = request.session["is_superuser"]

        users = User.objects.filter(is_active=True).exclude(username=username)
        if not users:
            users = {}

        return render(request, f"{template_path}user.html", {"users_list":users,"username":username,"admin":is_staff,"super_user":is_superuser})
    else:
        return redirect("home")

def add_user(request):
    if request.session.has_key("username"):
        username = request.session["username"]
        is_staff = request.session["is_staff"]
        is_superuser = request.session["is_superuser"]
        return render(request, f"{template_path}add_user.html", {"username":username,"admin":is_staff,"super_user":is_superuser})
    else:
        return redirect("home")

@csrf_exempt
def create_user(request):
    if request.session.has_key("username"):
        if request.method == "POST":
            try:
                request_by_is_superuser = request.session["is_superuser"]
                
                if request_by_is_superuser:
                    post_data = request.POST
 
                    username = post_data.get("username")
                    email = post_data.get("email")
                    password = post_data.get("password")
                    admin_or_superadmin = post_data.get("admin_or_superadmin")

                    if admin_or_superadmin == "admin":
                        is_staff = True
                        is_superuser = False
                    elif admin_or_superadmin == "superadmin":
                        is_staff = True
                        is_superuser = True
                    else:
                        is_staff = False
                        is_superuser = False

                    user = User.objects.create_user(
                        username=username.strip(),
                        email=email,
                        password=password,
                        is_staff=is_staff,
                        is_superuser=is_superuser
                    )
                    user.save()
                    return redirect("get_user")
                else:
                    return render(request,"login_response.html" ,{"response":"You cannot perform this operation!"})
            except Exception as err:
                return render(request,"login_response.html" ,{"response":f"Error: {err}"})
        else:
            return render(request,"login_response.html" ,{"response":"Get method not allowed!"})
    else:
        return redirect("home")
    
def view_user(request,pk):  
    if request.session.has_key("username"):
        request_by_user = request.session["username"]
        request_by_is_superuser = request.session["is_superuser"]
        request_by_is_admin = request.session["is_staff"]
        if request_by_is_superuser or request_by_is_admin:          
            user = User.objects.get(pk=pk)

            user_id=user.id
            name=user.username
            email=user.email
            is_staff=user.is_staff
            is_superuser=user.is_superuser
            
            return render(request, f"{template_path}edit_user.html" ,{"user_id":user_id,"name":name,"email":email,"is_staff":is_staff,"is_superuser":is_superuser,"username":request_by_user,"admin":request_by_is_admin,"super_user":request_by_is_superuser})
    else:
        return redirect("home")


def edit_user(request,pk):  
    if request.session.has_key("username"):
        if request.method == "POST":
            request_by_is_superuser = request.session["is_superuser"]
            request_by_is_admin = request.session["is_staff"]
            if request_by_is_superuser or request_by_is_admin:
                ed_name = request.POST.get("ed_username")
                ed_email = request.POST.get("ed_email")
                ed_admin_or_superadmin = request.POST.get("ed_admin_or_superadmin")

                user = User.objects.get(pk=pk)
                user.username = ed_name.strip()
                user.email = ed_email
                if ed_admin_or_superadmin == "admin":
                    user.is_staff = True
                    user.is_superuser = False
                elif ed_admin_or_superadmin == "superadmin":
                    user.is_staff = True
                    user.is_superuser = True
                else:
                    user.is_staff = False
                    user.is_superuser = False

                user.save()
            
                return redirect("get_user")
        else:
            return render(request,"login_response.html" ,{"response":"Get method not allowed!"})
    else:
        return redirect("home")


def delete_user(request,pk):  
    if request.session.has_key("username"):
        request_by_is_superuser = request.session["is_superuser"]
        if request_by_is_superuser:
            user = User.objects.get(pk=pk)
            user.delete()
            return redirect("get_user")
    else:
        return redirect("home")