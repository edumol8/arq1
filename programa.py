# Ejemplo de un sistema de archivos distribuido simple
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.archivos = {}

    def almacenar_archivo(self, nombre_archivo, contenido):
        self.archivos[nombre_archivo] = contenido

    def obtener_archivo(self, nombre_archivo):
        return self.archivos.get(nombre_archivo, None)

# Crear nodos
nodo_a = Nodo("A")
nodo_b = Nodo("B")
nodo_c = Nodo("C")

# Almacenar archivos en nodos
nodo_a.almacenar_archivo("archivo1.txt", "Contenido del archivo 1")
print(f"Archivo almacenado en nodo A")
nodo_b.almacenar_archivo("archivo2.txt", "Contenido del archivo 2")
print(f"Archivo almacenado en nodo B")
nodo_c.almacenar_archivo("archivo3.txt", "Contenido del archivo 3")
print("Archivo almacenado en nodo C")

# Función para obtener un archivo de cualquier nodo
def obtener_archivo_distribuido(nombre_archivo):
    for nodo in [nodo_a, nodo_b, nodo_c]:
        contenido = nodo.obtener_archivo(nombre_archivo)
        print(f"Buscando {nombre_archivo} en nodo {nodo.nombre}")
        if contenido:
            print(f"Archivo encontrado en nodo {nodo.nombre}")
            return contenido
    return "Archivo no encontrado"

# Obtener un archivo
print(obtener_archivo_distribuido("archivo2.txt"))





# 🧩 1. Múltiples nodos que cooperan

# Cada objeto de la clase Nodo representa una máquina independiente dentro del sistema distribuido.
# En un entorno real, esos nodos podrían ser:

# Computadoras diferentes conectadas por una red.

# Servidores que almacenan partes del sistema de archivos.

# En el programa, se crean tres nodos:

# nodo_a = Nodo("A")
# nodo_b = Nodo("B")
# nodo_c = Nodo("C")


# Esto simula una red de tres nodos que trabajan de forma conjunta.

# 🗂️ 2. Distribución de datos

# Cada nodo almacena una parte del conjunto total de archivos:

# nodo_a.almacenar_archivo("archivo1.txt", "Contenido del archivo 1")
# nodo_b.almacenar_archivo("archivo2.txt", "Contenido del archivo 2")
# nodo_c.almacenar_archivo("archivo3.txt", "Contenido del archivo 3")


# 👉 Esto representa la distribución de recursos o datos entre varios nodos, un principio básico en los sistemas distribuidos.

# 🔄 3. Cooperación para ofrecer un servicio común

# La función:

# def obtener_archivo_distribuido(nombre_archivo):
#     for nodo in [nodo_a, nodo_b, nodo_c]:
#         contenido = nodo.obtener_archivo(nombre_archivo)
#         if contenido:
#             return contenido


# recorre todos los nodos para encontrar el archivo solicitado.
# Es decir, el sistema completo (todos los nodos) coopera para ofrecer un servicio común: el acceso a archivos.

# Esto es exactamente lo que hacen sistemas distribuidos reales como HDFS (Hadoop Distributed File System) o Google File System (GFS).

# 🌐 4. Transparencia de acceso

# Desde la perspectiva del usuario, no importa en qué nodo está almacenado el archivo.
# El usuario simplemente llama a obtener_archivo_distribuido("archivo2.txt") y el sistema se encarga de buscarlo.

# Eso ilustra el principio de transparencia de ubicación, característico de los sistemas distribuidos.

# ⚙️ 5. Abstracción del entorno distribuido

# Aunque en este ejemplo todo ocurre dentro de un mismo programa (sin red real), el modelo lógico es el mismo:

# Nodos independientes

# Recursos distribuidos

# Coordinación y comunicación

# Servicio compartido

# Por eso se considera un ejemplo conceptual o didáctico de sistema distribuido.

# 🧠 En resumen
# Elemento	Representación en el código
# Nodos	Objetos Nodo
# Distribución	Archivos repartidos entre nodos
# Comunicación	Iteración y consultas entre nodos
# Transparencia	El usuario no sabe en qué nodo está el archivo
# Servicio común	Búsqueda y recuperación de archivos