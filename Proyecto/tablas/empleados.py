class Empleados:

    def mostrarDatos(self, cursor):
        cursor.execute(
            "SELECT id_empleado, id_cargo, nombre1, nombre2, apellido1, apellido2 FROM empleados;")
        # Con fetchall traemos todas las filas
        empleados = cursor.fetchall()
        # Recorrer e imprimir
        return empleados

    def ingresarDatos(self, idDato, dato1, dato2, dato3, dato4, dato5, cursor):
        consulta = "INSERT INTO empleados(id_empleado, id_cargo, nombre1, nombre2, apellido1, apellido2) VALUES (?, ?, ?, ?, ?, ?);"
        # Podemos llamar muchas veces a .execute con datos distintos
        cursor.execute(consulta, (idDato, dato1, dato2,
                       dato3, dato4, dato5))

    def actualizarDato(self, nuevoDato1, nuevoDato2, nuevoDato3, nuevoDato4, nuevoDato5, editarDato, cursor):
        consulta = "UPDATE  SET id_cargo = ?, nombre1 = ?, nombre2 = ?, apellido1 = ?, apellido2 = ? WHERE id_empleado = ?;"
        cursor.execute(
            consulta, (nuevoDato1, nuevoDato2, nuevoDato3, nuevoDato4, nuevoDato5, editarDato))

    def borrarDato(self, idElimimar, cursor):
        consulta = "DELETE FROM empleados WHERE id_empleado = ?;"
        cursor.execute(consulta, (idElimimar))
