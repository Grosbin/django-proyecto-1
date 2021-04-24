create database reposteria_prueba
GO

USE reposteria_prueba

create table proveedores
(
    id_proveedor INTEGER primary KEY,
    nombre1 VARCHAR(40) not null,
    nombre2 VARCHAR(40),
    apellido1 VARCHAR(40) not null,
    apellido2 VARCHAR(40)

)

ALTER TABLE proveedores ADD telefono VARCHAR(8)
ALTER TABLE productos ADD FOREIGN KEY(id_tipo_producto) REFERENCES tipos_productos(id_tipo_producto)

ALTER TABLE proveedores DROP COLUMN nombre2
ALTER TABLE proveedores DROP COLUMN apellido1
ALTER TABLE proveedores DROP COLUMN apellido2
GO

DELETE From inventario WHERE id_inventario = 1

SELECT *
FROM inventario

create table inventario
(
    id_inventario INTEGER PRIMARY key,
    descripcion VARCHAR(70) not NULL,
    unidad INTEGER not NULL,
    precio FLOAT not NULL,
    cantidad INTEGER not null
)

INSERT into inventario
VALUES(2, 'Fresas', 23, 45, 567)

create table proveedores_inventario
(
    id_proveedor INTEGER not null,
    idInventario INTEGER not null,
    FOREIGN key(id_proveedor) REFERENCES proveedores(id_proveedor),
    FOREIGN key(idInventario) REFERENCES inventario(id_inventario)
)

SELECT *
FROM proveedores_inventario

create table productos
(
    id_producto INTEGER PRIMARY KEY,
    descripcion VARCHAR(70) not null,
    costos_indirectos float not null,
    porcentaje_ganancia INTEGER not null,
    costo float not null,
    precio_unidad float not null
)

create table tipos_productos
(
    id_tipo_producto INTEGER PRIMARY KEY,
    nombre VARCHAR(25) not null

)

create table receta
(
    id_producto INTEGER not null,
    id_inventario INTEGER not null,
    cantidad INTEGER not null,
    PRIMARY KEY(id_producto, id_inventario),
    FOREIGN key(id_producto) REFERENCES productos(id_producto),
    FOREIGN key(id_inventario) REFERENCES inventario(id_inventario)
)

create table produccion_productos
(
    id_producto_produccion INTEGER PRIMARY KEY,
    cantidad INTEGER not NULL,
    fecha DATE not null,
    FOREIGN key(id_producto_produccion) REFERENCES productos(id_producto)
)

create table clientes
(
    id_cliente INTEGER PRIMARY key,
    nombre1 VARCHAR(30) not NULL,
    nombre2 VARCHAR(30),
    apellido1 VARCHAR(30) not null,
    apellido2 VARCHAR(30),
    direccion VARCHAR(50) not NULL,
    telefono VARCHAR(8)
)

create table cargos_empleados
(
    id_cargo INTEGER PRIMARY KEY,
    tipo VARCHAR(35) not null
)

INSERT INTO cargos_empleados
VALUES(1, 'Administrador')
INSERT INTO cargos_empleados
VALUES(2, 'Vendedor')
INSERT INTO cargos_empleados
VALUES(3, 'Repartidor')
INSERT INTO cargos_empleados
VALUES(4, 'Chef')
INSERT INTO cargos_empleados
VALUES(5, 'Auxiliar de Cocina')
INSERT INTO cargos_empleados
VALUES(6, 'Mercadeo')


create table empleados
(
    id_empleado INTEGER PRIMARY KEY,
    id_cargo INTEGER not null,
    nombre1 VARCHAR(30) not NULL,
    nombre2 VARCHAR(30),
    apellido1 VARCHAR(30) not null,
    apellido2 VARCHAR(30),
    FOREIGN key(id_cargo) REFERENCES cargos_empleados(id_cargo)
)

create table encargos
(
    id_encargos INTEGER PRIMARY KEY,
    id_empleado INTEGER not NULL,
    anticipo float not NULL,
    fecha_encargo date not NULL,
    fecha_entrega date not null,
    detalle VARCHAR(70),
    FOREIGN key(id_empleado) REFERENCES empleados(id_empleado)
)





create table detalle_encargo
(
    id_encargo INTEGER not NULL,
    id_producto INTEGER not NULL,
    cantidad INTEGER not NULL,
    primary KEY(id_encargo, id_producto)
)

create table ventas
(
    id_venta INTEGER,
    fecha DATE,
    id_empleado INTEGER not NULL,
    id_cliente INTEGER not NULL,
    id_producto INTEGER not null,
    precio_unidad FLOAT not NULL,
    cantidad INTEGER,
    PRIMARY key(id_venta, fecha),
    FOREIGN key(id_empleado) REFERENCES empleados(id_empleado),
    FOREIGN key(id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN key(id_producto) REFERENCES productos(id_producto)
)

create table facturas
(
    id_factura INTEGER,
    id_venta INTEGER,
    descripcion VARCHAR(70) not NULL,
    unidades INTEGER not NULL,
    precio_unidad INTEGER not null,
    fecha date,
    descuento FLOAT not null,
    total FLOAT not NULL,
    PRIMARY KEY(id_factura, id_venta, fecha),
    CONSTRAINT fk_venta_fecha FOREIGN KEY(id_venta, fecha) REFERENCES ventas(id_venta, fecha)
)

select name
from sysobjects
where type='U'


SELECT *
FROM inventario
SELECT *
FROM proveedores_inventario
SELECT *
From proveedores


CREATE VIEW vista_inventario_proveedores
AS
    SELECT cantidad
    FROM inventario


INSERT into proveedores
VALUES(2, 'Lecheria', '98857425')

INSERT into proveedores_inventario
VALUES(1, 2)


SELECT *
FROM vista_inventario_proveedor

drop view vista_inventario_proveedores

CREATE VIEW vista_inventario_proveedor
AS
    SELECT inventario.descripcion, proveedores.nombre1, inventario.id_inventario, proveedores.id_proveedor
    from proveedores_inventario INNER JOIN inventario ON proveedores_inventario.idInventario = inventario.id_inventario
        INNER JOIN proveedores ON proveedores_inventario.id_proveedor = proveedores.id_proveedor


