from django.urls import path
from . import views 


urlpatterns = [
    path('', views.hello, name='home'),
   path('', views.nosotros, name='Nosotros'),
   path('',views.servicios, name='servicios'),
   path('',views.Objetivos, name= 'Objetivos'),
   path('templates/index.html',views.Contactos, name= 'contactos'),
   path('templates/faqs.html', views.faqs, name='faqs'),
   path('templates/politicas.html', views.politicas, name='politicas'),
   path('guardar_pregunta/', views.guardar_pregunta, name='guardar_pregunta'),
]