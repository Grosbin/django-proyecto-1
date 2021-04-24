class TipoProducto:

    def mostrarDatos(self, cursor):
        cursor.execute("SELECT id_tipo_producto, nombre FROM tipos_productos;")
        # Con fetchall traemos todas las filas
        tip = cursor.fetchall()
        # Recorrer e imprimir
        return tip

    def ingresarDatos(self, id_tipo_producto, nombre, cursor):
        consulta = "INSERT INTO tipos_productos(id_tipo_producto, nombre) VALUES (?, ?);"
        # Podemos llamar muchas veces a .execute con datos distintos
        cursor.execute(consulta, (id_tipo_producto, nombre))

    def actualizarDato(self, nuevoNombre, cursor):
        consulta = "UPDATE tipos_productos SET nombre = ? WHERE id_tipo_producto = ?;"
        cursor.execute(
            consulta, (nuevoNombre))

    def borrarDato(self, idElimimar, cursor):
        consulta = "DELETE FROM tipos_productos WHERE id_tipo_producto = ?;"
        cursor.execute(consulta, (idElimimar))
