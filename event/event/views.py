from django.shortcuts import render
from event.models import Newuser
from django.contrib import messages

def Indexpage(request):
    return render(request,'index.html')

def Userreg(request):
    if request.method=='POST':
        Username=request.POST['Username']
        Email=request.POST['Email']
        Pwd=request.POST['Pwd']
        Age=request.POST['Age']
        Gender=request.POST['Gender']
        MartialStatus=request.POST['MartialStatus']
        Newuser(Username=Username,Email=Email,Pwd=Pwd,Age=Age,Gender=Gender,MartialStatus=MartialStatus).save()
        messages.success(request,'The New User'+' '+request.POST['Username']+ " Is saved successfully..!")
        return render(request,'Registration.html')
    else:
        return render(request,'Registration.html')


def loginpage(request):
    if request.method=="POST":
        try:
            Userdetails=Newuser.objects.get(Email=request.POST['Email'],Pwd=request.POST['Pwd'])
            print("Username=",Userdetails)
            request.session['Email']=Userdetails.Email
            return render(request,'index1.html')
        except Newuser.DoesNotExist as e:
            messages.success(request,'Username /  Password Invalid...!')
    
    return render(request,'Login.html')

def logout(request):
    try:
        del request.session['Email']
    except:
        return render(request,'Index.html')
    return render(request,'Index.html')

def index1(request):
    return render(request,'index1.html')