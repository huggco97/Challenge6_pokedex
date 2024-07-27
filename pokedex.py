import requests
import MySQLdb

# Conexión a la base de datos
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

conn = obtener_conexion()
cursor = conn.cursor()  

# Definición de la función para cargar Pokémon
def cargar_pokemon(id):
    api_url = f"https://pokeapi.co/api/v2/pokemon/{id}/"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        name = data.get('name')
        number = data.get('id')
        type = data['types'][0]['type']['name']
        moves = data['moves'][0]['move']['name']
       
        #Inserción en la base de datos
        cursor.execute("""
        INSERT INTO Pokemon (nombre_poke, tipo, habilidad, estadisticas)
        VALUES (%s, %s, %s, %s)
        """, (name, type, moves, number))
        
        conn.commit()

# Cargar Pokémon en un rango de IDs
for i in range(1, 152):
    cargar_pokemon(i)

# Cerrar cursor y conexión
cursor.close()
conn.close()
