from django.urls import path
from . import views as core_views
from django.conf import settings

urlpatterns = [
    path('', core_views.home, name="home"),
    path('about/', core_views.about, name="about"),
    path('store/', core_views.store, name="store"),
    path('contact/', core_views.contact, name="contact"),
    path('blog/', core_views.blog, name="blog"),
    path('test/', core_views.sample, name="sample"),
]

# Si estamos en modo DEBUG agregamos la ruta static de media a las urlpatterns
if settings.DEBUG:
   from django.conf.urls.static import static
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)