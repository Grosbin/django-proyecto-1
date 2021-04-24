CREATE DATABASE reposteria_imperial
GO

USE reposteria_imperial
GO


EXEC sp_help 'proveedores';
CREATE TABLE proveedores
(
    id_proveedor INTEGER IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(40) NOT NULL,
    telefono VARCHAR(8) NOT NULL,
    direccion VARCHAR(50),
    id_pago_proveedor INTEGER NOT NULL

)

INSERT INTO proveedores
VALUES('Inversiones Azucarita', '24123456', 'Col. El Carrizal', 1)

INSERT INTO proveedores
VALUES('Frutas Y Más', '23673643', 'Col. El Pedregal', 2)

INSERT INTO proveedores
VALUES('Chocoloco', '32343858', 'Col. Cerro Grande', 1)

CREATE TABLE metodo_pago
(
    id_pago INTEGER PRIMARY KEY,
    id_metodo INTEGER NOT NULL UNIQUE,
    tipo_metodo_descripcion VARCHAR(23)
)


CREATE TABLE pago_tarjeta
(
    codigo_tarjeta VARCHAR(19) PRIMARY KEY,
    facha DATE NOT NULL,
    id_metodo_pago INTEGER NOT NULL,
    banco VARCHAR(35) NOT NULL,
    codigo_pin VARCHAR(3) NOT NULL,
    fecha_vencimiento DATE NOT NULL,
    CONSTRAINT FK_metodo_tarjeta FOREIGN KEY(id_metodo_pago) REFERENCES metodo_pago(id_metodo) ON DELETE CASCADE ON UPDATE CASCADE,
    CHECK(id_metodo_pago = 2)

)

INSERT INTO pago_tarjeta
VALUES('1234-5678-4321-8765', '2021-04-14', 2, 'Banco Atlantida', '123', '2025-04-14')

CREATE TABLE pago_efectivo
(
    id_pago_efectivo INTEGER IDENTITY(1,1) PRIMARY KEY,
    fecha DATE NOT NULL,
    id_metodo_pago INTEGER NOT NULL,
    cantidad_efectivo FLOAT NOT NULL,
    cambio_efectivo FLOAT NOT NULL,
    CONSTRAINT Fk_metodo_efectivo FOREIGN KEY(id_metodo_pago) REFERENCES metodo_pago(id_metodo) ON DELETE CASCADE ON UPDATE CASCADE,
    CHECK(id_metodo_pago = 1)
)

INSERT INTO pago_efectivo
VALUES('2021-04-14', 1, 123, 50)

CREATE TABLE inventario
(
    id_inventario INTEGER IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(35) NOT NULL,
    descripcion VARCHAR(70) NOT NULL,
    unidad INTEGER NOT NULL,
    precio FLOAT NOT NULL,
    cantidad INTEGER NOT NULL
)



CREATE TABLE proveedores_inventario
(
    id_proveedor INTEGER NOT NULL,
    idInventario INTEGER NOT NULL,
    FOREIGN key(id_proveedor) REFERENCES proveedores(id_proveedor),
    FOREIGN key(idInventario) REFERENCES inventario(id_inventario)
)


CREATE TABLE tipos_productos
(
    id_tipo_producto INTEGER PRIMARY KEY,
    tipo_nombre VARCHAR(25) NOT NULL

)


CREATE TABLE productos
(
    id_producto INTEGER IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(35) NOT NULL,
    descripcion VARCHAR(70) NOT NULL,
    costos_indirectos float NOT NULL,
    porcentaje_ganancia INTEGER NOT NULL,
    existencia INT NOT NULL,
    costo FLOAT NOT NULL,
    precio_unidad FLOAT NOT NULL,
    id_tipo_producto INTEGER NOT NULL,
    CONSTRAINT FK_tipo_producto FOREIGN KEY(id_tipo_producto) REFERENCES tipos_productos(id_tipo_producto) ON DELETE CASCADE ON UPDATE CASCADE
)


EXEC sp_help 'ciudades';


CREATE TABLE recetas
(
    id_producto INTEGER NOT NULL,
    id_inventario INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    descripcion VARCHAR(70) NOT NULL,
    PRIMARY KEY(id_producto, id_inventario),
    CONSTRAINT FK_id_producto_receta FOREIGN key(id_producto) REFERENCES productos(id_producto) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT FK_id_inventario_receta FOREIGN key(id_inventario) REFERENCES inventario(id_inventario) ON DELETE CASCADE ON UPDATE CASCADE
)

CREATE TABLE produccion_productos
(
    id_producto_produccion INTEGER PRIMARY KEY,
    cantidad INTEGER NOT NULL,
    fecha DATE NOT NULL,
    CONSTRAINT FK_id_producto_produccion FOREIGN key(id_producto_produccion) REFERENCES productos(id_producto) ON DELETE CASCADE ON UPDATE CASCADE
)

CREATE TABLE departamentos
(
    id_departamento INTEGER IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(35) NOT NULL UNIQUE
)


CREATE TABLE ciudades
(
    id_ciudad INTEGER IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(35) NOT NULL,
    id_departamento INTEGER NOT NULL,
    CONSTRAINT FK_id_departamento FOREIGN KEY(id_departamento) REFERENCES departamentos(id_departamento)

)


CREATE TABLE clientes
(
    id_cliente INTEGER IDENTITY(1,1) PRIMARY KEY,
    nombre1 VARCHAR(30) NOT NULL,
    nombre2 VARCHAR(30),
    apellido1 VARCHAR(30) NOT NULL,
    apellido2 VARCHAR(30),
    direccion VARCHAR(50) NOT NULL,
    telefono VARCHAR(8),
    id_ciudad INTEGER NOT NULL,
    CONSTRAINT FK_id_ciudad FOREIGN KEY(id_ciudad) REFERENCES ciudades(id_ciudad)
)

CREATE TABLE cargos_empleados
(
    id_cargo INTEGER PRIMARY KEY,
    tipo VARCHAR(35) not null
)

CREATE TABLE salario
(
    id_salario INTEGER PRIMARY KEY,
    id_cargo INTEGER NOT NULL,
    cantidad FLOAT NOT NULL,
    CONSTRAINT FK_id_cargo_salario FOREIGN KEY(id_cargo) REFERENCES cargos_empleados(id_cargo) ON DELETE CASCADE ON UPDATE CASCADE
)


CREATE TABLE empleados
(
    id_empleado VARCHAR(15) PRIMARY KEY,
    id_cargo INTEGER NOT NULL,
    nombre1 VARCHAR(30) NOT NULL,
    nombre2 VARCHAR(30),
    apellido1 VARCHAR(30) NOT NULL,
    apellido2 VARCHAR(30),
    sexo VARCHAR(1),
    fecha_nacimiento DATE NOT NULL,
    CONSTRAINT FK_id_cargo FOREIGN key(id_cargo) REFERENCES cargos_empleados(id_cargo) ON DELETE CASCADE ON UPDATE CASCADE
)

CREATE TABLE encargos
(
    id_encargos INTEGER PRIMARY KEY,
    id_empleado VARCHAR(15) NOT NULL,
    id_entrega INTEGER NOT NULL,
    anticipo FLOAT NOT NULL,
    fecha_encargo DATE NOT NULL,
    fecha_entrega DATE NOT NULL,
    detalle VARCHAR(70),
    CONSTRAINT FK_id_empleados_encargos FOREIGN KEY(id_empleado) REFERENCES empleados(id_empleado) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT FK_id_entrega FOREIGN KEY(id_entrega) REFERENCES metodo_entrega(id_entrega) ON DELETE CASCADE ON UPDATE CASCADE
)


CREATE TABLE metodo_entrega
(
    id_entrega INTEGER PRIMARY KEY,
    id_metodo INTEGER NOT NULL UNIQUE,
    tipo_entrega_descripcion VARCHAR(35) NOT NULL,
)

CREATE TABLE metodo_local
(
    id_local_entrega INTEGER PRIMARY KEY,
    id_metodo INTEGER NOT NULL,
    estado_entrega BIT NOT NULL,
    CONSTRAINT FK_id_metodo FOREIGN KEY(id_metodo) REFERENCES metodo_entrega(id_metodo) ON DELETE CASCADE ON UPDATE CASCADE,
    CHECK(id_metodo = 1)
)

CREATE TABLE metodo_envio
(
    id_envio_entrega INTEGER PRIMARY KEY,
    id_metodo INTEGER NOT NULL,
    estado_entrega BIT NOT NULL,
    CONSTRAINT FK_id_metodo_envio FOREIGN KEY(id_metodo) REFERENCES metodo_entrega(id_metodo) ON DELETE CASCADE ON UPDATE CASCADE,
    CHECK(id_metodo = 2)
)




CREATE TABLE detalle_encargo
(
    id_encargo INTEGER NOT NULL,
    id_producto INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    PRIMARY KEY(id_encargo, id_producto)
)



CREATE TABLE ventas
(
    id_venta INTEGER IDENTITY(1,1),
    fecha DATE NOT NULL,
    id_empleado VARCHAR(15) NOT NULL,
    id_cliente INTEGER NOT NULL,
    id_producto INTEGER NOT null,
    precio_unidad FLOAT NOT NULL,
    cantidad INTEGER NOT NULL,
    id_pago INTEGER NOT NULL,
    PRIMARY KEY(id_venta, fecha),
    CONSTRAINT FK_venta_id_empleado FOREIGN KEY(id_empleado) REFERENCES empleados(id_empleado) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT FK_venta_id_cliente FOREIGN KEY(id_cliente) REFERENCES clientes(id_cliente) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT FK_venta_id_producto FOREIGN KEY(id_producto) REFERENCES productos(id_producto) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT FK_venta_id_pago FOREIGN KEY(id_pago) REFERENCES metodo_pago(id_pago) ON DELETE CASCADE ON UPDATE CASCADE

)

CREATE TABLE facturas
(
    id_factura INTEGER NOT NULL,
    id_venta INTEGER NOT NULL,
    fecha DATE NOT NULL,
    descripcion VARCHAR(70) NOT NULL,
    unidades INT NOT NULL,
    precio_unidad INT NOT NULL,
    porcentaje_descuento FLOAT NOT NULL,
    descuento AS (porcentaje_descuento / 100) PERSISTED NOT NULL,
    sub_total AS (unidades * precio_unidad) PERSISTED NOT NULL,
    total AS ((unidades * precio_unidad) - (((porcentaje_descuento / 100) * (unidades * precio_unidad)))) PERSISTED NOT NULL,
    PRIMARY KEY (id_factura, id_venta, fecha),
    CONSTRAINT fk_venta_fecha FOREIGN KEY(id_venta, fecha) REFERENCES ventas(id_venta, fecha)
)

select name
from sysobjects
where type='U'



INSERT INTO metodo_entrega
VALUES(1, 1, 'Metodo Local')
INSERT INTO metodo_entrega
VALUES(2, 2, 'Metodo Envio')

SELECT *
FROM metodo_entrega

INSERT INTO metodo_local
VALUES(1, 1, 0)
INSERT INTO metodo_envio
VALUES(2, 2, 0)


SELECT *
FROM metodo_local

SELECT *
FROM metodo_envio

INSERT INTO metodo_pago
VALUES(1, 1, 'Metodo Efectivo')
INSERT INTO metodo_pago
VALUES(2, 2, 'Metodo Tarjeta')


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


INSERT INTO salario
VALUES(1, 1, 25000)
INSERT INTO salario
VALUES(2, 2, 20000)
INSERT INTO salario
VALUES(3, 3, 15000)
INSERT INTO salario
VALUES(4, 4, 25000)
INSERT INTO salario
VALUES(5, 5, 20000)
INSERT INTO salario
VALUES(6, 6, 25000)

SELECT *
FROM salario
