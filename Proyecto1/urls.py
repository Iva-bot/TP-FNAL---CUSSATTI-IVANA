"""
URL configuration for Proyecto1 project.

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
from django.contrib import admin
from django.urls import path, include
from Proyecto1.views import saludo, otra_vista,dia_de_hoy,muestra_nombre,probando_template,agregar_producto
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppSanta/' , include('AppSanta.urls')),
    path('saludo/', saludo),
    path('otra_vista/' , otra_vista),
    path('dia/', dia_de_hoy),
    path('nombre/<nombre>', muestra_nombre),
    path('plantilla/',probando_template),
    path('agregar_producto/<nom>/<can>/',agregar_producto),
    path('users/' , include('users.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )