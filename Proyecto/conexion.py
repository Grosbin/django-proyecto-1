import pyodbc
# Nombre del servidor esto lo podemos encontrar en SQL Server Management Studio
direccion_servidor = 'localhost, 1433'
nombre_bd = 'reposteria_prueba'
nombre_usuario = 'sa'
password = '<r00tKhoal@>'
try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
    # OK! conexión exitosa
except Exception as e:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", e)
