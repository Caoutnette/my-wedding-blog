from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views


urlpatterns = [

    url(r'^date$', views.date_actuelle),
    url(r'^accueil$', views.home),
   

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)





