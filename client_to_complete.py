import requests
import time
import threading

def get_user_sync(user_id):
    """Función síncrona para obtener un usuario"""
    print(f"📤 Cliente: Solicitando usuario {user_id}...")
    start_time = time.time()
    
    try:
        # ESTA ES LA PARTE SÍNCRONA: el programa espera aquí
        response = requests.get(f'http://localhost:5000/api/users/{user_id}')
        end_time = time.time()
        
        if response.status_code == 200:
            user_data = response.json()
            print(f"✅ Cliente: Recibido usuario {user_id} - {user_data['data']['name']} "
                  f"(Tiempo: {end_time - start_time:.2f}s)")
            return user_data
        else:
            print(f"❌ Cliente: Error obteniendo usuario {user_id} - {response.json()}")
            return None
            
    except requests.exceptions.ConnectionError:
        print(f"💥 Cliente: No se pudo conectar al servidor para usuario {user_id}")
        return None

def create_user_sync(name, email):
    """Función síncrona para crear un usuario"""
    print(f"📤 Cliente: Creando usuario {name}...")
    start_time = time.time()
    
    user_data = {"name": name, "email": email}
    response = requests.post('http://localhost:5000/api/users', json=user_data)
    end_time = time.time()
    
    if response.status_code == 201:
        result = response.json()
        print(f"✅ Cliente: Usuario creado - {result['data']['name']} "
              f"(Tiempo: {end_time - start_time:.2f}s)")
        return result
    else:
        print(f"❌ Cliente: Error creando usuario - {response.json()}")
        return None

def demo_secuencial():
    """Demostración del comportamiento síncrono secuencial"""
    print("\n" + "="*50)
    print("DEMOSTRACIÓN SÍNCRONA SECUENCIAL")
    print("="*50)
    
    start_total = time.time()
    
    # Estas llamadas se ejecutan UNA DESPUÉS DE LA OTRA
    user1 = get_user_sync(1)
    user2 = get_user_sync(2)
    user3 = get_user_sync(3)
    
    end_total = time.time()
    print(f"\n⏰ Tiempo total secuencial: {end_total - start_total:.2f} segundos")

    
    

if __name__ == '__main__':
    # Primero asegúrate de que el servidor esté ejecutándose
    
    # Demostración secuencial
    demo_secuencial()
    
    # Pequeña pausa
    time.sleep(3)
    
    
    
    # Ejemplo de creación de usuario
    print("\n" + "="*50)
    print("CREACIÓN DE USUARIO")
    print("="*50)

    #TAREA 1:
    #En la sisguiente linea de codigo crea un nuevo usuario
    new_user = create_user_sync("Eduardo", "edumol@puce.com")
    
    #TAREA 2:
    # Si el usuario fue creado exitosamente, intenta obtenerlo y muestralo
    if new_user:
        # Obtenemos el usuario recién creado

        getid = new_user['data']['id']
        get_user_sync(getid)
