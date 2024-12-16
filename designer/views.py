from django.shortcuts import render
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import myproject
from django.contrib import messages
# sending the user detail to database
# def homepage(request):
#     return render(request,"main.html")



def userregister(request):
    if request.method=="POST":
        first=request.POST['fname']
        last=request.POST['lname']
        Email=request.POST['emails']
        p1=request.POST['pass1']
        p2=request.POST['pass2']

        if p1==p2:
            if len(p1)<8:
                messages.warning(request,"password should be greater then 8 digits  ..!")
                return render(request,"main.html")
            try:
                user=User.objects.get(username=first)
                # error={'ers':"user already exits.. !"}
                messages.warning(request,"User already exits..!")
                return render(request,'main.html')
            except User.DoesNotExist:
                
                push=User.objects.create(username=first,last_name=last,email=Email, password = make_password(p1))
                push.save()
                messages.success(request,"Thanks for be a member of our family!")
                return redirect ('login')

    return render(request,'main.html')

def userlogin(request):
    if request.method=="POST":
        nam=request.POST["user"]
        psswrd=request.POST['pass1']
      
        
        data=authenticate(username=nam,password=psswrd)
        if data is not None:
            login(request,data)
            messages.success(request,"You can upload your image and about your image and destination!")

            return render(request,'main.html')
        else:

            return redirect('login')

    return render(request,'logink.html')


def userlogout(request):
    logout(request)
    return redirect('home')
    

def showproject(request):
    return render(request,'project.html')


#update data

def userupdate(request,index):
    
    
    if request.method=="POST":
        uname=request.POST['usname']
        uemail=request.POST['usemail']
        ulastname=request.POST['uslname']
        passwrd=request.POST['pas1']
        pas=request.POST['pas2']
        if passwrd==pas:

            data=User.objects.filter(id=index).update(username=uname,last_name=ulastname,email=uemail,password=make_password(passwrd))

            return render(request,'main.html')
        
    return render(request,'useredit.html')


#upload image to database by user 

def uploadproject(request, index):
    print('index', index)
    uid = User.objects.get(id=index)  # Fetch the user based on the index
    print(uid.id)
    
    if request.method == "POST":
        titles = request.POST['ltitle']   
        descri = request.POST['ldesc']
        
        # Access the uploaded file from request.FILES
        if 'lupload' in request.FILES:
            photoes = request.FILES['lupload']
        
            if uid.is_authenticated:
                # Pass the user to the userid field when creating the project
                data = myproject.objects.create(title=titles, desc=descri, photo=photoes, userid=uid)
                data.save()
                messages.success(request, "Project uploaded successfully.")
                return render(request,'blogpage.html')
        else:
            messages.error(request, "Please upload a valid file.")
    
    return render(request, 'upload.html')




# show project image in webpage
@login_required(login_url="login")
def showp(request):
    data=myproject.objects.all()

    return render(request,'blogpage.html',{"data":data})


def user_name(request):
    data=User.objects.all()
    return render(request,"main.html",{"data":data})