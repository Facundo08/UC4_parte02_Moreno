from django.shortcuts import render, HttpResponse
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
    return render(request, 'listar_cursos.html')

def agregar_curso(request):
    return render(request, 'agregar_curso.html')

def listar_carreras(request):
    return render(request, 'listar_carreras.html')

def agregar_carrera(request):
    return render(request, 'agregar_carrera.html')

def index(request):
    return render(request, "index.html")

def saludo(request):
    return render(request,'saludo.html')

