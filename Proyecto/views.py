from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from django.shortcuts import render
from django.shortcuts import redirect
from Proyecto.conexion import conexion
from Proyecto.tablas.productos import Productos
from Proyecto.tablas.tipo_producto import TipoProducto
from Proyecto.tablas.empleados import Empleados
from Proyecto.tablas.proveedores import Proveedores
from Proyecto.tablas.inventario import Inventarios
from Proyecto.tablas.inventario_proveedor import InventariosProveedores

producto = Productos()
tipos_productos = TipoProducto()
empleado = Empleados()
proveedor = Proveedores()
inventario_conexion = Inventarios()
inventario_proveedor_conexion = InventariosProveedores()

"""
def buscar(request):
    if request.GET["prd"]:
        mensaje = "Articulo busacado: %r" % request.GET["prd"]
        producto = request.GET["prd"]
        if len(producto) > 20:
            message = "Texto de busqueda demaciado grande"
        else:
            cliente = Clientes.objects.filter(primernombre__icontains=producto)
            return render(request, "resultado.html", {"clientes": cliente, "query": producto})
    else:
        mensaje = "No ha intruducido nada"

    return HttpResponse(mensaje)
"""


def index(request):
    return render(request, "base.html")


def inicio(request):
    with conexion.cursor() as cursor:
        prod = producto.mostrarDatos(cursor)
        tip = tipos_productos.mostrarDatos(cursor)

    return render(request, "inicio.html", {"productos": prod, "tipos": tip})


def productos(request):
    with conexion.cursor() as cursor:
        prod = producto.mostrarDatos(cursor)

    return render(request, "productos.html", {"productos": producto.mostrarDatos(cursor)})


def producto_enviar(request):
    with conexion.cursor() as cursor:

        id_producto = request.POST["id"]
        descripcion = request.POST["descripcion"]
        costos_indirectos = request.POST["costos_indirectos"]
        porcentaje_ganancia = request.POST["porcentaje_ganancia"]
        costo = request.POST["costos"]
        precio_unidad = request.POST["precio_unidad"]
        id_tipo_producto = request.POST["id_tipo_producto"]

        producto.ingresarDatos(id_producto, descripcion, costos_indirectos,
                               porcentaje_ganancia, costo, precio_unidad, id_tipo_producto, cursor)

        return redirect('/productos/')


def borrar_producto(request, id):
    with conexion.cursor() as cursor:

        producto.borrarDato(id, cursor)

        return redirect('/productos/')

 # ///////////////// TIPO PRODUCTO


def tipo_producto(request):
    with conexion.cursor() as cursor:
        tipProducto = tipos_productos.mostrarDatos(cursor)
        return render(request, "tipos_productos.html", {"tipos_productos": tipProducto})


def tipo_producto_enviar(request):
    with conexion.cursor() as cursor:

        id_tipo_producto = request.POST["id"]
        nombre = request.POST["nombre"]

        tipos_productos.ingresarDatos(id_tipo_producto, nombre, cursor)

        return redirect('/tipo_producto/')


def borrar_tipo_producto(request, id):
    with conexion.cursor() as cursor:

        tipos_productos.borrarDato(id, cursor)

        return redirect('/tipo_producto/')


# ///////////////// EMPLEADOS


def empleados(request):
    with conexion.cursor() as cursor:
        empleados = empleado.mostrarDatos(cursor)
        return render(request, "empleados.html", {"empleados": empleados})


def empleados_enviar(request):
    with conexion.cursor() as cursor:

        id_empleado = request.POST["id"]
        id_cargo = request.POST["id_cargo"]
        nombre1 = request.POST["nombre1"]
        nombre2 = request.POST["nombre2"]
        apellido1 = request.POST["apellido1"]
        apellido2 = request.POST["apellido2"]

        empleado.ingresarDatos(id_empleado, id_cargo,
                               nombre1, nombre2, apellido1, apellido2, cursor)

        return redirect('/empleados/')


def empleado_borrar(request, id):
    with conexion.cursor() as cursor:

        empleado.borrarDato(id, cursor)

        return redirect('/empleados/')


# ///////////////// PROVEEDORES


def proveedores(request):
    with conexion.cursor() as cursor:
        proveedores = proveedor.mostrarDatos(cursor)
        return render(request, "proveedores.html", {"proveedores": proveedores})


def proveedor_enviar(request):
    with conexion.cursor() as cursor:

        id_proveedor = request.POST["id"]
        nombre = request.POST["nombre"]
        telefono = request.POST["telefono"]

        proveedor.ingresarDatos(id_proveedor, nombre, telefono, cursor)

        return redirect('/proveedores/')


def proveedor_borrar(request, id):
    with conexion.cursor() as cursor:

        proveedor.borrarDato(id, cursor)

        return redirect('/proveedores/')


# ///////////////// IVENTARIO


def inventario(request):
    with conexion.cursor() as cursor:
        inventarios = inventario_conexion.mostrarDatos(cursor)
        inventarios_proveedores = inventario_proveedor_conexion.datos_inventario_proveedor(
            cursor)

        cantidades = inventario_conexion.cantidades(cursor)

        nombres = inventario_conexion.nombres(cursor)

        precios = inventario_conexion.precio(cursor)

        unidades = inventario_conexion.unidad(cursor)

        return render(request, "inventario_prueba.html", {"inventarios": inventarios, "inventarios_proveedores": inventarios_proveedores, "cantidades": cantidades, "nombres": nombres, "precios": precios, "unidades": unidades})


def inventario_enviar(request):
    with conexion.cursor() as cursor:

        id_inventario = request.POST["id"]
        descripcion = request.POST["descripcion"]
        unidad = request.POST["unidad"]
        precio = request.POST["precio"]
        cantidad = request.POST["cantidad"]
        id_proveedor = request.POST["id_proveedor"]

        inventario_conexion.ingresarDatos(
            id_inventario, descripcion, unidad, precio, cantidad, cursor)

        inventario_proveedor_conexion.ingresarDatos(
            id_proveedor, id_inventario, cursor)

        return redirect('/inventario/')


def inventario_borrar(request, id):
    with conexion.cursor() as cursor:
        inventario_conexion.borrarDato(id, cursor)

        return redirect('/inventario/')
