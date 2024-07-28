import MySQLdb
from pokedex import obtener_conexion

conn = obtener_conexion()
cursor = conn.cursor()  

def validar_relacion(id_entrenador, id_pokemon):
    conn = obtener_conexion()
    if conn:
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute("SELECT * FROM Intermedia WHERE id_entrenador = %s AND id_pokemon = %s", (id_entrenador, id_pokemon))
            relacion = cursor.fetchone()
            return relacion is not None
        except MySQLdb.Error as e:
            print(f"Error al consultar la base de datos: {e}")
            return False
        finally:
            cursor.close()
            conn.close()

def agregar_batalla(id_entrenador1, id_entrenador2, id_pokemon1, id_pokemon2, fecha, resultado):
    if not validar_relacion(id_entrenador1, id_pokemon1):
        print(f"El entrenador {id_entrenador1} no posee el Pokémon {id_pokemon1}.")
        return
    if not validar_relacion(id_entrenador2, id_pokemon2):
        print(f"El entrenador {id_entrenador2} no posee el Pokémon {id_pokemon2}.")
        return

    conn = obtener_conexion()
    if conn:
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute('''INSERT INTO Batalla (id_entrenador1, id_entrenador2, id_pokemon1, id_pokemon2, fecha, resultado) VALUES (%s, %s, %s, %s, %s, %s)''', 
                           (id_entrenador1, id_entrenador2, id_pokemon1, id_pokemon2, fecha, resultado))
            conn.commit()
        except MySQLdb.Error as e:
            print(f"Error al insertar en la base de datos: {e}")
        finally:
            cursor.close()
            conn.close()

def mostrar_batallas():
    conn = obtener_conexion()
    if conn:
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute("SELECT * FROM Batalla")
            lista_batallas = cursor.fetchall()
            return lista_batallas
        except MySQLdb.Error as e:
            print(f"Error al consultar la base de datos: {e}")
            return []
        finally:
            cursor.close()
            conn.close()

def eliminar_batalla(id_batalla):
    conn = obtener_conexion()
    if conn:
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute("DELETE FROM Batalla WHERE id_batalla = %s", (id_batalla,))
            conn.commit()
        except MySQLdb.Error as e:
            print(f"Error al eliminar de la base de datos: {e}")
        finally:
            cursor.close()
            conn.close()

agregar_batalla(2, 3, 12, 11, '2024-07-21', 'gano Ash')
agregar_batalla(2, 3, 2, 3, '2024-07-21', 'gano Brock')
# eliminar_batalla(8)
# eliminar_batalla(9)