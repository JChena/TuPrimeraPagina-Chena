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

