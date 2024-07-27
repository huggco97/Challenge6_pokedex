
import MySQLdb

def obtener_conexion():
    try:
        return MySQLdb.connect(
            host="localhost", 
            user="root", 
            passwd="skylinegtr34", 
            db="pokedexDB"
        )
    except MySQLdb.OperationalError as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def agregar_entrenador(nombre_entr, ciudad, medallas):
    conn = obtener_conexion()
    if conn:
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute('''INSERT INTO Entrenador (nombre_entr, ciudad, medallas) VALUES (%s, %s, %s)''', (nombre_entr, ciudad, medallas))
            conn.commit()
        except MySQLdb.Error as e:
            print(f"Error al insertar en la base de datos: {e}")
        finally:
            cursor.close()
            conn.close()

def mostrar_entrenadores():
    conn = obtener_conexion()
    if conn:
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute("SELECT * FROM Entrenador")
            lista_entrenadores = cursor.fetchall()
            return lista_entrenadores
        except MySQLdb.Error as e:
            print(f"Error al consultar la base de datos: {e}")
            return []
        finally:
            cursor.close()
            conn.close()

def actualizar_entrenador(id, nombre_entr, ciudad, medallas):
    conn = obtener_conexion()
    if conn:
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute("UPDATE Entrenador SET nombre_entr = %s, ciudad = %s, medallas = %s WHERE id_entrenador = %s", (nombre_entr, ciudad, medallas, id))
            conn.commit()
        except MySQLdb.Error as e:
            print(f"Error al actualizar en la base de datos: {e}")
        finally:
            cursor.close()
            conn.close()

def eliminar_entrenador(id):
    conn = obtener_conexion()
    if conn:
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute("DELETE FROM Entrenador WHERE id_entrenador = %s", (id,))
            conn.commit()
        except MySQLdb.Error as e:
            print(f"Error al eliminar de la base de datos: {e}")
        finally:
            cursor.close()
            conn.close()

# Llamando a la función para agregar un entrenador
agregar_entrenador("Ash Ketchum", "Pueblo Paleta", 9)
agregar_entrenador("Brock", "Pueblo Paleta", 8)
agregar_entrenador("Kevin", "Luque", 10)
agregar_entrenador("Hugo", "Pueblo frutilla", 10)
agregar_entrenador("Marcos", "Pueblo luque", 10)

# Llamando a la funcion para actualizar un pokemon
#actualizar_entrenador(5,"Marcos", "Pueblo frutilla", 9)

#Lamado a la funcion para eliminar un pokemon 
# eliminar_entrenador(1)
# eliminar_entrenador(3)
# eliminar_entrenador(4)



# Mostrando la tabla de entrenadores
entrenadores = mostrar_entrenadores()

# Crear un conjunto vacío para rastrear entrenadores únicos
entrenadores_vistos = set()

if entrenadores:
    for entrenador in entrenadores:
        # Crear una tupla única para cada entrenador
        entrenador_tupla = (entrenador['id_entrenador'], entrenador['nombre_entr'], entrenador['ciudad'], entrenador['medallas'])
        
        # Verificar si la tupla ya está en el conjunto
        if entrenador_tupla not in entrenadores_vistos:
            # Si no está, agregarla al conjunto y mostrar los datos
            entrenadores_vistos.add(entrenador_tupla)
            print(f"ID: {entrenador['id_entrenador']}, Nombre: {entrenador['nombre_entr']}, Ciudad: {entrenador['ciudad']}, Medallas: {entrenador['medallas']}")
else:
    print("No se encontraron entrenadores.")

