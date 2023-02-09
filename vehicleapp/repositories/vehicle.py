from django.shortcuts import render, redirect
from vehicleapp.models import Vehicle

template_path = "vehicle/"

def get_vehicle(request):
    if request.session.has_key("username"):
        username = request.session["username"]
        is_staff = request.session["is_staff"]
        is_superuser = request.session["is_superuser"]

        vehicles = Vehicle.objects.all()
        if not vehicles:
            vehicles = {}
        
        return render(request, f"{template_path}vehicle.html", {"vehicle_list":vehicles,"username":username,"admin":is_staff,"super_user":is_superuser})
    else:
        return redirect("home")


def add_vehicle(request):
    if request.session.has_key("username"):
        username = request.session["username"]
        is_staff = request.session["is_staff"]
        is_superuser = request.session["is_superuser"]
        return render(request, f"{template_path}add_vehicle.html", {"username":username,"admin":is_staff,"super_user":is_superuser})
    else:
        return redirect("home")

def create_vehicle(request):
    if request.session.has_key("username"):
        if request.method == "POST":
            try:
                request_by_is_superuser = request.session["is_superuser"]
                
                if request_by_is_superuser:
                    post_data = request.POST
                    vc_number = post_data.get("vc_number")
                    vc_model = post_data.get("vc_model")
                    vc_desc = post_data.get("vc_desc")
                    vc_type = post_data.get("vc_type")

                    user = Vehicle.objects.create(
                        number=vc_number,
                        model=vc_model.strip(),
                        description=vc_desc.strip(),
                        type=vc_type
                    )
                    user.save()
                    return redirect("get_vehicle")
                else:
                    return render(request,"login_response.html" ,{"response":"You cannot perform this operation!"})
            except Exception as err:
                return render(request,"login_response.html" ,{"response":f"Error: {err}"})
        else:
            return render(request,"login_response.html" ,{"response":"Get method not allowed!"})
    else:
        return redirect("home")


def view_vehicle(request,pk):
    if request.session.has_key("username"):
        request_by_user = request.session["username"]
        request_by_is_superuser = request.session["is_superuser"]
        request_by_is_admin = request.session["is_staff"]
        if request_by_is_superuser or request_by_is_admin:          
            vehicle = Vehicle.objects.get(pk=pk)

            vehicle_id=vehicle.id
            number=vehicle.number
            model=vehicle.model
            desc=vehicle.description
            type=vehicle.type
            
            return render(request, f"{template_path}edit_vehicle.html" ,{"vehicle_id":vehicle_id,"number":number,"model":model,"desc":desc,"type":type,"username":request_by_user,"admin":request_by_is_admin,"super_user":request_by_is_superuser})
    else:
        return redirect("home")

def edit_vehicle(request,pk):
    if request.session.has_key("username"):
        if request.method == "POST":
            request_by_is_superuser = request.session["is_superuser"]
            request_by_is_admin = request.session["is_staff"]
            if request_by_is_superuser or request_by_is_admin:

                post_data = request.POST
                vc_number = post_data.get("vc_number")
                vc_model = post_data.get("vc_model")
                vc_desc = post_data.get("vc_desc")
                vc_type = post_data.get("vc_type")


                vehicle = Vehicle.objects.get(pk=pk)
                vehicle.number = vc_number
                vehicle.model = vc_model.strip()
                vehicle.description = vc_desc.strip()
                vehicle.type = vc_type
                
                vehicle.save()
            
                return redirect("get_vehicle")
        else:
            return render(request,"login_response.html" ,{"response":"Get method not allowed!"})
    else:
        return redirect("home")


def delete_vehicle(request,pk):  
    if request.session.has_key("username"):
        request_by_is_superuser = request.session["is_superuser"]
        if request_by_is_superuser:
            vehicle = Vehicle.objects.get(pk=pk)
            vehicle.delete()
            return redirect("get_vehicle")
    else:
        return redirect("home")