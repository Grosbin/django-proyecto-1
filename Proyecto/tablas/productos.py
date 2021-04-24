class Productos:

    def mostrarDatos(self, cursor):
        cursor.execute(
            "SELECT id_producto, descripcion, costos_indirectos, porcentaje_ganancia, costo, precio_unidad, id_tipo_producto FROM productos;")
        # Con fetchall traemos todas las filas
        Productos = cursor.fetchall()
        # Recorrer e imprimir
        return Productos

    def ingresarDatos(self, id_producto, descripcion, costos_indirectos, procentaje_ganancia, costo, precio_unidad, id_tipo_producto, cursor):
        consulta = "INSERT INTO productos(id_producto, descripcion, costos_indirectos, porcentaje_ganancia, costo, precio_unidad, id_tipo_producto) VALUES (?, ?, ?, ?, ?, ?, ?);"
        # Podemos llamar muchas veces a .execute con datos distintos
        cursor.execute(consulta, (id_producto, descripcion,
                       costos_indirectos, procentaje_ganancia, costo, precio_unidad, id_tipo_producto))

    def actualizarDato(self, nuevoNombre, nuevoPrecio, nuevoStock, idEditar, cursor):
        consulta = "UPDATE Productos SET Nombre = ?, Precio = ?, Stock = ? WHERE Id_Producto = ?;"
        '''nuevo_nombre = dato
        id_editar = idPro'''
        cursor.execute(
            consulta, (nuevoNombre, nuevoPrecio, nuevoStock, idEditar))

    def borrarDato(self, idElimimar, cursor):
        consulta = "DELETE FROM Productos WHERE Id_Producto = ?;"
        cursor.execute(consulta, (idElimimar))
