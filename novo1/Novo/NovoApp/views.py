from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login  # Asegúrate de importar authenticate
from .models import Producto  # Asegúrate de que Producto esté importado correctamente

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

def buscar_productos(request):
    query = request.GET.get('query', '')  # Obtén el término de búsqueda desde la URL
    if query:
        # Busca productos cuyo nombre o descripción contenga el término de búsqueda
        productos = Producto.objects.filter(nombre__icontains=query)  # Filtra por nombre de producto
    else:
        productos = Producto.objects.all()  # Si no se proporcionó término, muestra todos los productos

    # Pasa los productos encontrados a la plantilla
    return render(request, 'resultado.html', {'productos': productos, 'query': query})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirige al índice después de un inicio de sesión exitoso
        else:
            return render(request, 'login.html', {'error': 'Credenciales incorrectas'})
    else:
        return render(request, 'login.html')
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente después del registro
            return redirect('index')  # Redirige a la página de inicio o a donde desees
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

def cart_view(request):
    # Lógica para mostrar los artículos en el carrito
    return render(request, 'carrito.html') 

def checkout(request):
    return render(request, 'checkout.html')