from django.urls import path
# el . significa importar del directorio actual
from . import views

#  Assignar con corchetes significa lista, esto permite que haya varios elementos
urlpatterns = [
    path('', views.index, name='index'), 
    path('proceso', views.proceso, name='proceso'),
    # path('suma', views.suma, name='suma'),
    path('bienvenida', views.bienvenida, name='bienvenida'),
    path('suma', views.suma, name='suma'),
    path('resta', views.resta, name='resta'), 
    path('multiplicacion', views.multiplicacion, name='multiplicacion'),  
    path('division', views.division, name='division'),
]

# esto es un endpoint