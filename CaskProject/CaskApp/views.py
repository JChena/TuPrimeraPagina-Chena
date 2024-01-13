from django.shortcuts import render, redirect
from . import models
from . import forms

def index(request):
    return render(request, 'CaskApp/index.html')

def producto_list(request):
    consulta = models.Producto.objects.all()
    contexto = {'productos': consulta}
    return render(request, 'CaskApp/producto_list.html', contexto)

def producto_form(request):
    if request.method == "POST":
        form = forms.ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = forms.ProductoForm()
    return render(request, 'CaskApp/producto_form.html', {'form': form})

def cliente_list(request):
    consulta = models.Cliente.objects.all()
    contexto = {'clientes': consulta}
    return render(request, 'CaskApp/cliente_list.html', contexto)

def cliente_form(request):
    if request.method == "POST":
        form = forms.ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = forms.ClienteForm()
    return render(request, 'CaskApp/cliente_form.html', {'form': form})

def cata_list(request):
    consulta = models.Cata.objects.all()
    contexto = {'catas': consulta}
    return render(request, 'CaskApp/cata_list.html', contexto)

def cata_form(request):
    if request.method == "POST":
        form = forms.CataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cata_list')
    else:
        form = forms.CataForm()
    return render(request, 'CaskApp/cata_form.html', {'form': form})

