# aca se definen las rutas de la app blogs

from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('', views.root),
    path('blogs', views.index),
    path('blogs/new', views.new),
    path('blogs/create',views.create),
    path('blogs/<number>',views.show),
    path('blogs/<number>/edit',views.edit),
    path('blogs/<number>/delete',views.destroy),
    path('json',views.bonus),
    
    #inicio ejercicio
    path('adios', views.adios),
    path('saludar/<name>', views.saludar),  
    path('edad/<name>/<int:age>', views.edad),  
    
]