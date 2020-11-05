from django.shortcuts import render

# Create your views here.
def portada(request):
    return render(request, 'portada.html',{})

def registro(request):
	return render(request, 'registro.html',{})

def principal(request):
    return render(request, 'principal.html',{})

def inicio(request):
    return render(request, 'inicio.html',{})
    
def  nosotros(request):
    return render(request, 'nosotros.html',{})
    
def  Admin(request):
    return render(request, 'Admin.html',{})
    
def index(request):
    return render(request, 'index.html',{})
    
def compra(request):
    return render(request, 'compra.html',{})
    

