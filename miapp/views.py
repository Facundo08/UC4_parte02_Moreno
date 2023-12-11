from django.shortcuts import render, HttpResponse
#from .views import listar_cursos, crear_curso
from .models import Course
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
layout = """
    <h1> Proyecto Web (LP3) | Flor Cerdán </h1>
    <hr/>
    <ul>
        <li>
            <a href="/listar_cursos">Cursos</a>
        </li>
        <li>
            <a href="/agregar_curso">Crear curso</a>
        </li>
        <li>
            <a href="/listar_carreras">Carreras</a>
        </li>
        <li>
            <a href="/agregar_carrera">Crear Carrera</a>
        </li>
    </ul>
    <hr/>
"""

def listar_cursos(request):
    courses = Course.objects.all()
    return render(request, 'listar_cursos.html', {'courses': courses})
    #return render(request, 'listar_cursos.html')
def crear_curso(request):
    if request.method == 'POST':
        code = request.POST['code']
        name = request.POST['name']
        hour = request.POST['hour']
        credits = request.POST['credits']
        state = request.POST['state']

        Course.objects.create(
            code=code,
            name=name,
            hour=hour,
            credits=credits,
            state=state
        )

        messages.success(request, 'Curso creado exitosamente')
        return redirect('listar_cursos')

    return render(request, 'crear_curso.html')
#def agregar_curso(request):
#    return render(request, 'agregar_curso.html')

def listar_carreras(request):
    return render(request, 'listar_carreras.html')

def agregar_carrera(request):
    return render(request, 'agregar_carrera.html')

def index(request):
    return render(request, "index.html")

def saludo(request):
    return render(request,'saludo.html')

