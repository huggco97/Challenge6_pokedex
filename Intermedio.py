import MySQLdb
from pokedex import obtener_conexion

conn = obtener_conexion()
cursor = conn.cursor()  

def agregar_intermedia(id_entrenador, id_pokemon):
    conn = obtener_conexion()
    if conn:
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        try:
            # Verificar si el Pokémon ya está asociado con un entrenador
            cursor.execute("SELECT * FROM Intermedia WHERE id_pokemon = %s", (id_pokemon,))
            resultado = cursor.fetchone()
            if resultado:
                print("Este Pokémon ya está asociado con otro entrenador.")
                return
            
            # Agregar relación en la tabla intermedia
            cursor.execute('''INSERT INTO Intermedia (id_entrenador, id_pokemon) VALUES (%s, %s)''', (id_entrenador, id_pokemon))
            conn.commit()
        except MySQLdb.Error as e:
            print(f"Error al insertar en la base de datos: {e}")
        finally:
            cursor.close()
            conn.close()

def mostrar_intermedia():
    conn = obtener_conexion()
    if conn:
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute("SELECT * FROM Intermedia")
            lista_intermedia = cursor.fetchall()
            return lista_intermedia
        except MySQLdb.Error as e:
            print(f"Error al consultar la base de datos: {e}")
            return []
        finally:
            cursor.close()
            conn.close()

def eliminar_intermedia(id_intermedia):
    conn = obtener_conexion()
    if conn:
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute("DELETE FROM Intermedia WHERE id_intermedia = %s", (id_intermedia,))
            conn.commit()
        except MySQLdb.Error as e:
            print(f"Error al eliminar de la base de datos: {e}")
        finally:
            cursor.close()
            conn.close()

agregar_intermedia(1,1)
agregar_intermedia(2, 2)
agregar_intermedia(2, 12)
agregar_intermedia(3, 3)
agregar_intermedia(3,11)
#agregar_intermedia(3, 2)

equipo = mostrar_intermedia()
if equipo:
    for intermedia in equipo:
        print(f"ID: {intermedia['id_inter']}, Entrenador: {intermedia['id_entrenador']}, Pokemon: {intermedia['id_pokemon']}")
else:
    print("No se encontraron intermedio.")