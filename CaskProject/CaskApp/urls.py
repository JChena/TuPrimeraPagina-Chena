"""
URL configuration for CaskProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('producto/list', views.producto_list, name='producto_list'),
    path('producto/form', views.producto_form, name='producto_form'),
    path('cliente/list', views.cliente_list, name='cliente_list'),
    path('cliente/form', views.cliente_form, name='cliente_form'),
    path('cata/list', views.cata_list, name='cata_list'),
    path('cata/form', views.cata_form, name='cata_form'),
]
