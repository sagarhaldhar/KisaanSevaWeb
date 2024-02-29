from django.shortcuts import render
from django.http import HttpResponse
from .models import farmer,scholar

# Create your views here.

def farmerlogin(request):
  return render(request,"farmer/farmerlogin.html",{})

def scholarlogin(request):
  return render(request,"scholar/scholarlogin.html",{})

def add_farmer(request):
  if request.method == "POST":
    farmer_name = request.POST.get("Farmer_name")
    contact_num = request.POST.get("Contact_num")
    email_id = request.POST.get("Email_id")
    password = request.POST.get("Password")
  f = farmer()
  f.Farmer_name = farmer_name
  f.Contact_num = contact_num
  f.Email_id = email_id
  f.Password = password
  f.save()
  return render(request,"farmer/farmerlogin.html",{})
def add_scholar(request):
  if request.method == "POST":
    scholar_name = request.POST.get("Scholar_name")
    contact_num = request.POST.get("Contact_num")
    email_id = request.POST.get("Email_id")
    password = request.POST.get("Password")
  s = scholar()
  s.Scholar_name = scholar_name
  s.Contact_num = contact_num
  s.Email_id = email_id
  s.Password = password
  s.save()

  return render(request,"scholar/scholarlogin.html",{})

