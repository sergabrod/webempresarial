from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
   return render(request, "core/index.html", {'active_home': 'active'})


def about(request):
   return render(request, "core/about.html", {'active_about': 'active'})


def services(request):
   return render(request, "core/services.html", {'active_services': 'active'})


def store(request):
   return render(request, "core/store.html", {'active_store': 'active'})


def contact(request):
   return render(request, "core/contact.html", {'active_contact': 'active'})


def blog(request):
   return render(request, "core/blog.html", {'active_blog': 'active'})


def sample(request):
   return render(request, "core/sample.html")