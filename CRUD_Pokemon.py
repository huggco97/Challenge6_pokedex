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

def agregar_pokemon(nombre_poke, tipo, habilidad, estadisticas):
    conn = obtener_conexion()
    if conn:
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute('''INSERT INTO Pokemon (nombre_poke, tipo, habilidad, estadisticas) VALUES (%s, %s, %s, %s)''', (nombre_poke, tipo, habilidad, estadisticas))
            conn.commit()
        except MySQLdb.Error as e:
            print(f"Error al insertar en la base de datos: {e}")
        finally:
            cursor.close()
            conn.close()

def mostrar_pokemones():
    conn = obtener_conexion()
    if conn:
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute("SELECT * FROM Pokemon")
            lista_pokemones = cursor.fetchall()
            return lista_pokemones
        except MySQLdb.Error as e:
            print(f"Error al consultar la base de datos: {e}")
            return []
        finally:
            cursor.close()
            conn.close()

def actualizar_pokemon(id, nombre_poke, tipo, habilidad, estadisticas):
    conn = obtener_conexion()
    if conn:
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute("UPDATE Pokemon SET nombre_poke = %s, tipo = %s , habilidad = %s, estadisticas = %s WHERE id_pokemon = %s", (nombre_poke, tipo, habilidad, estadisticas, id))
            conn.commit()
        except MySQLdb.Error as e:
            print(f"Error al actualizar en la base de datos: {e}")
        finally:
            cursor.close()
            conn.close()

def eliminar_pokemon(id):
    conn = obtener_conexion()
    if conn:
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute("DELETE FROM Pokemon WHERE id_pokemon = %s", (id,))
            conn.commit()
        except MySQLdb.Error as e:
            print(f"Error al eliminar de la base de datos: {e}")
        finally:
            cursor.close()
            conn.close()

# Llamando a la funcion para agregar un pokemon
#agregar_pokemon("perro viralata", "delmer", "ataque sorpresa", 15)

# Llamando a la funcion para actualizar un pokemon
#actualizar_pokemon(153, "perro viralata", "delmer", "ataque sorpresa", 100)

#Lamado a la funcion para eliminar un pokemon 
eliminar_pokemon(152)

# Mostrando la tabla de pokemones
pokemones = mostrar_pokemones()
if pokemones:
    for pokemon in pokemones:
        print(f"ID: {pokemon['id_pokemon']}, Nombre: {pokemon['nombre_poke']}, Tipo: {pokemon['tipo']}, Estadisticas: {pokemon['estadisticas']}")
else:
    print("No se encontraron pokemones.")