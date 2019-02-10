from django.shortcuts import render
from django.template import Template, Context


from django.http import HttpResponse

# Create your views here.
def home(request):
   return render(request, "home.html", {})

def music(request):
   return render(request, "music.html", {})

def visuals(request):
   return render(request, "visuals.html", {})

def about(request):
   return render(request, "about.html", {})

def contact(request):
   return render(request, "contact.html", {})

