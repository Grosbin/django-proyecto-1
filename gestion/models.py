# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CargosEmpleados(models.Model):
    id_cargo = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'cargos_empleados'


class Clientes(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    nombre1 = models.CharField(max_length=30)
    nombre2 = models.CharField(max_length=30, blank=True, null=True)
    apellido1 = models.CharField(max_length=30)
    apellido2 = models.CharField(max_length=30, blank=True, null=True)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'


class DetalleEncargo(models.Model):
    id_encargo = models.IntegerField(primary_key=True)
    id_producto = models.IntegerField()
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detalle_encargo'
        unique_together = (('id_encargo', 'id_producto'),)


class Empleados(models.Model):
    id_empleado = models.IntegerField(primary_key=True)
    id_cargo = models.ForeignKey(
        CargosEmpleados, models.DO_NOTHING, db_column='id_cargo')
    nombre1 = models.CharField(max_length=30)
    nombre2 = models.CharField(max_length=30, blank=True, null=True)
    apellido1 = models.CharField(max_length=30)
    apellido2 = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleados'


class Encargos(models.Model):
    id_encargos = models.IntegerField(primary_key=True)
    id_empleado = models.ForeignKey(
        Empleados, models.DO_NOTHING, db_column='id_empleado')
    anticipo = models.FloatField()
    fecha_encargo = models.DateField()
    fecha_entrega = models.DateField()
    detalle = models.CharField(max_length=70, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'encargos'


class Facturas(models.Model):
    id_factura = models.IntegerField(primary_key=True)
    id_venta = models.ForeignKey(
        'Ventas', models.DO_NOTHING, db_column='id_venta', related_name='idventa')
    descripcion = models.CharField(max_length=70)
    unidades = models.IntegerField()
    precio_unidad = models.IntegerField()
    fecha = models.ForeignKey(
        'Ventas', models.DO_NOTHING, db_column='fecha', related_name='idfecha')
    descuento = models.FloatField()
    total = models.FloatField()

    class Meta:
        managed = False
        db_table = 'facturas'
        unique_together = (('id_factura', 'id_venta', 'fecha'),)


class Inventario(models.Model):
    id_inventario = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=70)
    unidad = models.IntegerField()
    precio = models.FloatField()
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inventario'


class ProduccionProductos(models.Model):
    id_producto_produccion = models.ForeignKey(
        'Productos', models.DO_NOTHING, db_column='id_producto_produccion', primary_key=True)
    cantidad = models.IntegerField()
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'produccion_productos'


class Productos(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=70)
    costos_indirectos = models.FloatField()
    porcentaje_ganancia = models.IntegerField()
    costo = models.FloatField()
    precio_unidad = models.FloatField()

    class Meta:
        managed = False
        db_table = 'productos'


class Proveedores(models.Model):
    id_proveedor = models.IntegerField(primary_key=True)
    nombre1 = models.CharField(max_length=40)
    nombre2 = models.CharField(max_length=40, blank=True, null=True)
    apellido1 = models.CharField(max_length=40)
    apellido2 = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedores'


class ProveedoresInventario(models.Model):
    id_proveedor = models.ForeignKey(
        Proveedores, models.DO_NOTHING, db_column='id_proveedor')
    # Field name made lowercase.
    idinventario = models.ForeignKey(
        Inventario, models.DO_NOTHING, db_column='idInventario')

    class Meta:
        managed = False
        db_table = 'proveedores_inventario'


class Receta(models.Model):
    id_producto = models.ForeignKey(
        Productos, models.DO_NOTHING, db_column='id_producto', primary_key=True)
    id_inventario = models.ForeignKey(
        Inventario, models.DO_NOTHING, db_column='id_inventario')
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'receta'
        unique_together = (('id_producto', 'id_inventario'),)


class Ventas(models.Model):
    id_venta = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    id_empleado = models.ForeignKey(
        Empleados, models.DO_NOTHING, db_column='id_empleado')
    id_cliente = models.ForeignKey(
        Clientes, models.DO_NOTHING, db_column='id_cliente')
    id_producto = models.ForeignKey(
        Productos, models.DO_NOTHING, db_column='id_producto')
    precio_unidad = models.FloatField()
    cantidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ventas'
        unique_together = (('id_venta', 'fecha'),)
