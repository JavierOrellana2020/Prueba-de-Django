from django.urls import path
from .import views

urlpatterns = [
        path('',views.portada ,name=''),
        path('principal',views.principal ,name='principal'),
        path('registro',views.registro ,name='registro'),
        path('inicio',views.inicio ,name='inicio'),
        path('nosotros',views.nosotros ,name='nosotros'),
        path('Admin', views.Admin, name='Admin'),
        path('index.html',views.index, name='index.html'),
        path('compra.html',views.compra,name='compra.html'),
      
]

#127.0.0.1:8000/

#127.0.0.1:8000/principal

#127.0.0.1:8000/registro

#127.0.0.1:8000/inicio

#127.0.0.1:8000/nosotros

#127.0.0.1:8000/Admin

#127.0.0.1:8000/index

#127.0.0.1:8000/compra.html

