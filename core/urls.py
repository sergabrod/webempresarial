from django.urls import path
from . import views as core_views


urlpatterns = [
    path('', core_views.home, name="home"),
    path('about/', core_views.about, name="about"),
    path('store/', core_views.store, name="store"),
    path('contact/', core_views.contact, name="contact"),
    path('test/', core_views.sample, name="sample"),
]
