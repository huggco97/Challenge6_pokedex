import MySQLdb
from pokedex import obtener_conexion

conn = obtener_conexion()
cursor = conn.cursor()  

def eliminar_pokemon_y_relaciones(id_pokemon):
    conn = obtener_conexion()
    if conn:
        cursor = conn.cursor()
        try:
            # Eliminar registros relacionados en la tabla Intermedia
            cursor.execute('''DELETE Intermedia FROM Intermedia
                              JOIN Pokemon ON Intermedia.id_pokemon = Pokemon.id_pokemon
                              WHERE Pokemon.id_pokemon = %s''', (id_pokemon,))
            
            # Eliminar registros relacionados en la tabla Batalla
            cursor.execute('''DELETE Batalla FROM Batalla
                              JOIN Pokemon ON (Batalla.id_pokemon1 = Pokemon.id_pokemon OR Batalla.id_pokemon2 = Pokemon.id_pokemon)
                              WHERE Pokemon.id_pokemon = %s''', (id_pokemon,))
            
            # Eliminar el Pokémon de la tabla principal
            cursor.execute("DELETE FROM Pokemon WHERE id_pokemon = %s", (id_pokemon,))
            
            conn.commit()
        except MySQLdb.Error as e:
            print(f"Error al eliminar de la base de datos: {e}")
        finally:
            cursor.close()
            conn.close()

#--------------------------------------------------------------------------------------------------------------


def mostrar_pokemones_y_entrenadores():
    conn = obtener_conexion()
    if conn:
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        try:
            query = '''SELECT p.id_pokemon, p.nombre_poke, e.nombre_entr, e.ciudad
                       FROM Intermedia i
                       JOIN Pokemon p ON i.id_pokemon = p.id_pokemon
                       JOIN Entrenador e ON i.id_entrenador = e.id_entrenador'''
            cursor.execute(query)
            resultados = cursor.fetchall()
            return resultados
        except MySQLdb.Error as e:
            print(f"Error al consultar la base de datos: {e}")
            return []
        finally:
            cursor.close()
            conn.close()

def mostrar_batallas_detalladas():
    conn = obtener_conexion()
    if conn:
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        try:
            query = '''SELECT b.id_batalla, e1.nombre_entr AS entrenador1, e2.nombre_entr AS entrenador2,
                       p1.nombre_poke AS pokemon1, p2.nombre_poke AS pokemon2, b.fecha, b.resultado
                       FROM Batalla b
                       JOIN Entrenador e1 ON b.id_entrenador1 = e1.id_entrenador
                       JOIN Entrenador e2 ON b.id_entrenador2 = e2.id_entrenador
                       JOIN Pokemon p1 ON b.id_pokemon1 = p1.id_pokemon
                       JOIN Pokemon p2 ON b.id_pokemon2 = p2.id_pokemon'''
            cursor.execute(query)
            resultados = cursor.fetchall()
            return resultados
        except MySQLdb.Error as e:
            print(f"Error al consultar la base de datos: {e}")
            return []
        finally:
            cursor.close()
            conn.close()

#--------------------------------------------------------------------------------------------------------------------

# Eliminar un Pokémon y sus registros relacionados
eliminar_pokemon_y_relaciones(11)  

# Mostrar Pokémon y sus entrenadores
# pokemones_y_entrenadores = mostrar_pokemones_y_entrenadores()
# for item in pokemones_y_entrenadores:
#     print(f"ID Pokémon: {item['id_pokemon']}, Nombre Pokmon: {item['nombre_poke']}, Entrenador: {item['nombre_entr']}, Ciudad: {item['ciudad']}")

# Mostrar detalles de las batallas
batallas_detalladas = mostrar_batallas_detalladas()
for batalla in batallas_detalladas:
    print(f"ID Batalla: {batalla['id_batalla']}, Entrenador 1: {batalla['entrenador1']}, Entrenador 2: {batalla['entrenador2']}, Pokémon 1: {batalla['pokemon1']}, Pokémon 2: {batalla['pokemon2']}, Fecha: {batalla['fecha']}, Resultado: {batalla['resultado']}")
