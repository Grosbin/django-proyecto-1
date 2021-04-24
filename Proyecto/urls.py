"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from Proyecto.views import index, inicio, productos, producto_enviar, borrar_producto
from Proyecto.views import tipo_producto, tipo_producto_enviar, borrar_tipo_producto
from Proyecto.views import empleados, empleados_enviar, empleado_borrar
from Proyecto.views import proveedores, proveedor_enviar, proveedor_borrar
from Proyecto.views import inventario, inventario_enviar, inventario_borrar
# Agregado modo prueba
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('', inicio, name='inicio'),
    # Productos
    path('productos/', productos, name='productos'),
    path('producto/enviar/', producto_enviar, name='proEnviar'),
    path('producto/borrar/<int:id>', borrar_producto, name='borrarProducto'),
    # Tipos Productos
    path('tipo_producto/', tipo_producto, name='tipo_producto'),
    path('tipos_producto/enviar/', tipo_producto_enviar, name='tipEnviar'),
    path('tipo_producto/borrar/<int:id>',
         borrar_tipo_producto, name='borrar_tipo_producto'),
    # Empleados
    path('empleados/', empleados, name='empleados'),
    path('empleados/enviar/', empleados_enviar, name='enviar_empleado'),
    path('empleados/borrar/<int:id>',
         empleado_borrar, name='borrar_empleado'),
    # Empleados
    path('proveedores/', proveedores, name='proveedores'),
    path('proveedores/enviar/', proveedor_enviar, name='enviar_proveedor'),
    path('proveedores/borrar/<int:id>',
         proveedor_borrar, name='borrar_proveedor'),
    # Empleados
    path('inventario/', inventario, name='inventario'),
    path('inventario/enviar/', inventario_enviar, name='enviar_inventario'),
    path('inventario/borrar/<int:id>',
         inventario_borrar, name='borrar_inventario'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
