"""
URL configuration for proyecto001 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from miapp import views
from .views import listar_cursos, crear_curso


urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('myapp.urls')),
    path('', views.index, name = "index"),
    path('list/', listar_cursos, name='listar_cursos'),
    path('create/', crear_curso, name='crear_curso'),
    #path('cursos/', views.listar_cursos, name='listar_cursos'),
    path('crear_curso/', views.agregar_curso, name='agregar_curso'),
    path('carreras/', views.listar_carreras, name='listar_carreras'),
    path('crear_carrera/', views.agregar_carrera, name='agregar_carrera'),
]
