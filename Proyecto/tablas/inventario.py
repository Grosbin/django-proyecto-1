class Inventarios:

    def mostrarDatos(self, cursor):
        cursor.execute(
            "SELECT id_inventario, descripcion, unidad, precio, cantidad FROM inventario;")
        # Con fetchall traemos todas las filas
        inventario = cursor.fetchall()
        # Recorrer e imprimir
        return inventario

    def cantidades(self, cursor):
        cursor.execute("SELECT cantidad FROM inventario;")
        cantidad = cursor.fetchall()
        dato = []
        for can in cantidad:
            dato += can
        return dato

    def nombres(self, cursor):
        cursor.execute("SELECT id_inventario FROM inventario;")
        inventario = cursor.fetchall()
        dato = []
        for idInv in inventario:
            dato += idInv
        return dato

    def precio(self, cursor):
        cursor.execute("SELECT precio FROM inventario;")
        inventario = cursor.fetchall()
        dato = []
        for idInv in inventario:
            dato += idInv
        return dato

    def unidad(self, cursor):
        cursor.execute("SELECT unidad FROM inventario;")
        inventario = cursor.fetchall()
        dato = []
        for idInv in inventario:
            dato += idInv
        return dato

    def ingresarDatos(self, idDato, dato1, dato2, dato3, dato4, cursor):
        consulta = "INSERT INTO inventario(id_inventario, descripcion, unidad, precio, cantidad) VALUES (?, ?, ?, ?, ?);"
        # Podemos llamar muchas veces a .execute con datos distintos
        cursor.execute(consulta, (idDato, dato1, dato2, dato3, dato4))

    def actualizarDato(self, nuevoDato1, nuevoDato2, idEditar,  cursor):
        consulta = "UPDATE inventario SET descripcion = ?, unidad = ?, precio = ?, cantidad = ? WHERE id_inventario = ?;"
        cursor.execute(
            consulta, (nuevoDato1, nuevoDato2, idEditar))

    def borrarDato(self, idElimimar, cursor):
        consulta = "DELETE FROM inventario WHERE id_inventario = ?;"
        cursor.execute(consulta, (idElimimar))
