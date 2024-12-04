from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def perifericos(request):
    return render(request, 'perifericos.html')

def laptops(request):
    return render(request, 'laptops.html')

def componentes(request):
    return render(request, 'componentes.html')

def contacto(request):
    return render(request, 'contacto.html')