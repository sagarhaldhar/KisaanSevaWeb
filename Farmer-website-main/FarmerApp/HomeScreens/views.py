from django.shortcuts import render
from .models import Testimonial
from .models import Feedback
from .models import ContactUsForm

# Create your views here.
def home(request):
  return render(request,"home/index.html",{})

def aboutus(request):
  return render(request,"about/aboutsUs.html",{})

def blogs(request):
  return render(request,"blog/blogs.html",{})

def contactus(request):
  return render(request,"contact/contactus.html",{})

def testimonial(request):
  testi = Testimonial.objects.all()
  return render(request,"testimonial/testimonials.html",{
    'testi' : testi
  })

def feedback(request):
  if request.method == "POST":
    f = Feedback()
    f.name = request.POST.get("name")
    f.feedback = request.POST.get("feedback")
    f.picture = request.FILES['picture']
    f.save()
    return render(request,"home/index.html",{})
  
def ScholarUI(request):
  return render(request,"ScholarUI/welcome.html",{})

def contactusform(request):
  if request.method == "POST":
    c = ContactUsForm()
    c.Name = request.POST.get("name")
    c.Email = request.POST.get("email")
    c.Message = request.POST.get("message")
    c.save()
    return render(request,"home/index.html",{})