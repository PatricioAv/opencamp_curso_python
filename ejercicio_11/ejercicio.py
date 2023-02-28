import sqlite3

def main():

    def conexion():
        with sqlite3.connect('ejercicio.db') as conn:
            return conn


    def crear_tabla():
        conn = conexion()
        cursor = conn.cursor()
        query = """CREATE TABLE IF NOT EXISTS alumnos (
                   id INTEGER PRIMARY KEY,
                   nombre TEXT NOT NULL,
                   apellido TEXT NOT NULL);"""
        cursor.execute(query)


    def crear_alumno(id_alumno, nombre, apellido):
        conn = conexion()
        cursor = conn.cursor()
        query = "INSERT OR IGNORE INTO alumnos(id, nombre, apellido) VALUES(?, ?, ?)"
        cursor.execute(query, (id_alumno, nombre, apellido))
        conn.commit()
    

    def buscar_alumno(nombre):
        conn = conexion()
        cursor = conn.cursor()
        query = f"SELECT * FROM alumnos WHERE nombre=='{nombre}'"
        rows = cursor.execute(query)#, nombre)
        return rows.fetchall()

    crear_tabla()

    crear_alumno(1, 'Juan', 'Aravena')
    crear_alumno(2, 'Juana', 'Carabina')
    crear_alumno(3, 'Juan', 'Calabaza')
    crear_alumno(4, 'Ester', 'Fuentes')
    crear_alumno(5, 'Roberto', 'Espinoza')
    crear_alumno(6, 'Mauricio', 'Cifuentes')
    crear_alumno(7, 'Esteban', 'Dido')
    crear_alumno(8, 'Ester', 'Molina')
    crear_alumno(9, 'Fernando', 'Cilantro')
    crear_alumno(10, 'Juana', 'Remates')
    
    # Imprimir restutado de la busqueda por nombre
    print(buscar_alumno('Fernando'))
    #print(buscar_alumno('Juan'))
    #print(buscar_alumno('Juana'))
    #print(buscar_alumno('Esteban'))

if __name__ == "__main__":
    main()
