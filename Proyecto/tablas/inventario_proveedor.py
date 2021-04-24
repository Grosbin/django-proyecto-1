class InventariosProveedores:

    def datos_inventario_proveedor(self, cursor):
        cursor.execute("SELECT * FROM vista_inventario_proveedor;")
        inventario_proveedor = cursor.fetchall()
        return inventario_proveedor

    def ingresarDatos(self, dato1, dato2, cursor):
        consulta = "INSERT INTO proveedores_inventario(id_proveedor, IdInventario) VALUES (?, ?);"
        # Podemos llamar muchas veces a .execute con datos distintos
        cursor.execute(consulta, (dato1, dato2))

    def borrarDato(self, idElimimar, dato2Eliminar, cursor):
        consulta = "DELETE FROM inventario_proveedor WHERE id_inventario = ? AND id_proveedor = ?;"
        cursor.execute(consulta, (idElimimar, dato2Eliminar))
