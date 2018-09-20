from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
   return HttpResponse("<h1>Web Empresarial</h1><h2>Home</h2>")


def about(request):
   return HttpResponse("<h1>Web Empresarial</h1><h2>About</h2>")


def services(request):
   return HttpResponse("<h1>Web Empresarial</h1><h2>Services</h2>")


def store(request):
   return HttpResponse("<h1>Web Empresarial</h1><h2>Store</h2>")


def contact(request):
   return HttpResponse("<h1>Web Empresarial</h1><h2>Contact</h2>")


def blog(request):
   return HttpResponse("<h1>Web Empresarial</h1><h2>Blog</h2>")


def sample(request):
   return HttpResponse("<h1>Web Empresarial</h1><h2>Sample</h2>")