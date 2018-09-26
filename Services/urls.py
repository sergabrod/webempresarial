from django.urls import path
from . import views as service_views
from django.conf import settings

urlpatterns = [
    path('services/', service_views.services, name="services"),
]

# Si estamos en modo DEBUG agregamos la ruta static de media a las urlpatterns
if settings.DEBUG:
   from django.conf.urls.static import static
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)