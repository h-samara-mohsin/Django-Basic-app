from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    # return HttpResponse("this is home page")
    context = {
        'variable1':"this is sent",
        'variable2':"this is received"
    }
    messages.success(request, "this is a test msg")
    return render(request,"index.html",context)

def about(request):
    # return HttpResponse("this is about page")
    return render(request,"about.html")

def services (request):
    # return HttpResponse("this is services page")
    return render(request,"services.html")

def contact(request):
    # return HttpResponse("this is contact us pg")
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(name = name,email=email,phone = phone,desc=desc, date= datetime.today())
        contact.save()
        messages.success(request, "your msg has been sent.")
    return render(request, "contact.html")