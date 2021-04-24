CREATE DATABASE reposteria_imperial
GO

USE reposteria_imperial
GO

CREATE TABLE proveedores
(
    id_proveedor INTEGER IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(40) NOT NULL,
    telefono VARCHAR(8) NOT NULL,
    direccion VARCHAR(50),
    id_pago_proveedor INTEGER NOT NULL

);
GO

