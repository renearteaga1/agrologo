from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db.models import Avg

from .models import Categoria, Producto, Rate
from .forms import ProductoForm

# Create your views here.
def indexView(request):

    context = {
    'name' : 'Agrologo',
    }
    return render(request, 'index/index.html', context)

def lista(request, template_name):

    productos = Producto.objects.all()
    producto_form = ProductoForm()
    context = {
        'productos' : productos,
        'producto_form' : producto_form
    }
    data = dict()
    data['lista'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def nuevo_producto(request):
    if request.method == 'POST':
        pf = ProductoForm(request.POST)
        if pf.is_valid():
            name = pf.cleaned_data['name']
            print(name)
            print(request.POST.get('name'))
            pf.save()
            producto_form = ProductoForm()
            return lista(request, 'index/table.html')
        else:
            producto_form = ProductoForm()
            print('data sucia')
    return redirect('inicio:index')

def delete_producto(request, pk):
    if request.method == 'POST':
        print('siii delete')
        print(pk)
        producto = Producto.objects.get(id=pk)
        producto.delete()
        return lista(request, 'index/table.html')
    data = dict()
    p = Producto.objects.get(id=pk)
    context = {
        'p':p
    }
    data['delete'] = render_to_string('index/delete_modal.html', context, request=request)
    return JsonResponse(data)
    return redirect('inicio:index')
