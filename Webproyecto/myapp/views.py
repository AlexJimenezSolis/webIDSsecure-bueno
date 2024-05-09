from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import PreguntaNoRespondida
from .forms import PreguntaForm
# Create your views here.

def hello(request):
    title = 'Django'
    return render(request,'index.html', {
        'title': title
    })
def nosotros(request):
    title='Nosotros'
    return render(request,'index.html',{
        'title':title
    })
def servicios(request):
    title='Que ofrecemos'
    return render(request,'index.html',{
        'title':title
    })   
def Objetivos(request):
    title='Objetivos'
    return render(request,'index.html',{
        'title':title
    })

def Contactos(request):
    title='COMO CONTACTARNOS'
    return render(request,'index.html',{
        'title':title
    })
def faqs(request):
    return render(request, 'faqs.html')

def politicas(request):
    return render(request, 'politicas.html')


def guardar_pregunta(request):
    if request.method == 'POST':
        form = PreguntaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faqs')
    else:
        form = PreguntaForm()
        return render(request, 'faqs.html', {'form': form})