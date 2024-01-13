from django import forms

from . import models

class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields ="__all__"

class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = "__all__"

class CataForm(forms.ModelForm):
    class Meta:
        model = models.Cata
        fields = "__all__"