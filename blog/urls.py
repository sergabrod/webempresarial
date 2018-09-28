from django.urls import path
from . import views as blogs_views


urlpatterns = [
    path('', blogs_views.blog, name="blog"),
    path('category/<int:category_id>/', blogs_views.category, name="category"),
]
