class Proveedores:

    def mostrarDatos(self, cursor):
        cursor.execute(
            "SELECT id_proveedor, nombre1, telefono FROM proveedores;")
        # Con fetchall traemos todas las filas
        prov = cursor.fetchall()
        # Recorrer e imprimir
        return prov

    def ingresarDatos(self, idDato, dato1, dato2, cursor):
        consulta = "INSERT INTO proveedores(id_proveedor, nombre1, telefono) VALUES (?, ?, ?);"
        # Podemos llamar muchas veces a .execute con datos distintos
        cursor.execute(consulta, (idDato, dato1, dato2))

    def actualizarDato(self, nuevoDato1, nuevoDato2, idEditar,  cursor):
        consulta = "UPDATE proveedores SET nombre1 = ?, telefono = ? WHERE id_proveedor = ?;"
        cursor.execute(
            consulta, (nuevoDato1, nuevoDato2, idEditar))

    def borrarDato(self, idElimimar, cursor):
        consulta = "DELETE FROM proveedores WHERE id_proveedor = ?;"
        cursor.execute(consulta, (idElimimar))
