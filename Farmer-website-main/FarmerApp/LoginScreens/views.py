from django.shortcuts import render,redirect
from .models import farmer,scholar
from django.contrib import messages
from django.contrib.auth import authenticate,login
# Create your views here.

def farmerlogin(request):
  return render(request,"farmer/farmerlogin.html",{})

def scholarlogin(request):
  return render(request,"scholar/scholarlogin.html",{})

def add_farmer(request):
  if request.method == "POST":
    f = farmer()
    f.Farmer_name = request.POST.get("Farmer_name")
    f.Contact_num = request.POST.get("Contact_num")
    f.Email_id = request.POST.get("Email_id")
    f.Password = request.POST.get("Password")
    
  # checking existing -
    check_existing = farmer.objects.filter(Farmer_name=f.Farmer_name) and farmer.objects.filter(Contact_num = f.Contact_num) and farmer.objects.filter(Email_id = f.Email_id) and farmer.objects.filter(Password = f.Password).exists()
    if check_existing:
      messages.error(request,"User already exists! Please login...")
      return redirect('/login/farmerlogin/')
  
    else:
      f.save()
      messages.success(request,'successfully saved...')
    # return redirect('login/farmerlogin/')
      return render(request,"home/index.html",{})

# scholar form validation :-
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
  # checking existing -
  check_existing = scholar.objects.filter(Scholar_name=scholar_name) and scholar.objects.filter(Contact_num = contact_num) and scholar.objects.filter(Email_id = email_id) and scholar.objects.filter(Password = password).exists()
  if check_existing:
    messages.error(request,"User already exists! Please login...")
    return redirect('/login/scholarlogin/')

  else:
    s.save()
    messages.success(request,'successfully saved..Please login')
    return redirect('/login/scholarlogin/')



def loginfarmer(request):
  if request.method == "POST":
    f = farmer()
    f.Email_id = request.POST.get("EmailId")
    f.Password = request.POST.get("Logpassword")

  # checking existing -
  check_existing =farmer.objects.filter(Email_id = f.Email_id) and farmer.objects.filter(Password = f.Password).exists()

  if check_existing:
    return render(request,"home/index.html",{})
  else:
    messages.success(request,"please register yourself first....")
    return redirect('/login/farmerlogin/')
  
def loginscholar(request):
  if request.method == "POST":
    emailsc = request.POST.get("scholarEmail")
    passw = request.POST.get("scholarPassword")
  f = scholar()
  f.Email_id = emailsc
  f.Password = passw

  # checking existing -
  check_existing =scholar.objects.filter(Email_id = emailsc) and scholar.objects.filter(Password = passw).exists()

  if check_existing:
    return redirect('/scholar/')
  else:
    messages.error(request,"please register yourself first....")
    return redirect('/login/scholarlogin/')