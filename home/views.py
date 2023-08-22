from django.shortcuts import render,HttpResponse
from .models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {'name': 'Indu','course': 'Django','he':'super'}
    return render(request,"home.html",context)

def about(request):
    return render(request,"about.html")
def projects(request):
    return render(request,"projects.html")
def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        #print(name,email,phone,desc)
        if len(phone) == 10:
            contact = Contact(name=name,email=email,phone=phone,desc=desc)
            contact.save()
            print("saved")
            messages.success(request, "The message sent successfully.")
        else:
            messages.warning(request, "Please enter valid phonenumber.")
        
    return render(request,"contact.html")
