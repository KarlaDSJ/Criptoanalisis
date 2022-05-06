import hashlib

def lee_bd(path):
    """ Lee la base de

    Args:
        path (_type_): _description_

    Returns:
        _type_: _description_
    """
    users = []    
    with open(path) as f:
        for line in f:
            info = line.split('$')
            #0 - usuario, 1 - salt, 2- hash            
            last = (bytes.fromhex(info[1]), bytes.fromhex(info[2].strip()))
            users.append(last)
    return users

def encuentra_contra(sal, contra_hash, contras):
    """ Encuentra una de las contraseñas de la base de datos hackeada
    usando sha256

    Args:
        sal (bytes): sal
        contra_hash (bytes): cotraseña hasheada
        contras (list): lista de contraseñas en bytes

    Returns:
        bytes: contraseña usada en bytes
    """
    for i in contras: 
        salida1 = hashlib.sha256(sal+i).digest()
        salida2 = hashlib.sha256(i+sal).digest()
        if salida1 == contra_hash or salida2 == contra_hash:
            return i

def get_batch(batchSize):
    """ Para la lista de todas las posibles contraseñas en español

    Args:
        batchSize (int): tamaño de los lotes
    """
    # Lista de diccionarios que representará el batch de documentos.        
    batch = []
    # Líneas procesadas hasta el momento.
    processedLines = 0

    with open("passwords.txt", 'rb') as infile:
        for line in infile:            
            batch.append(line[:-1])
            processedLines += 1
            if processedLines == batchSize:
                processedLines = 0
                yield batch
                batch = []
        if processedLines < batchSize:
            yield batch

def desencripta_una(id):
    """ Desencripta una contraseña de la base de datos hackeada

    Args:
        id (int): número de usuario

    Returns:
        bytes: contraseña desencriptada o None
    """
    gen = get_batch(1000)
    for batch in gen:
        x = encuentra_contra(users[id][0], users[id][1], batch)
        if x != None:
            return x
    print("no respuesta")

def desencripta():
    """ Desencripta todas las contraseñas de la base de datos hackeada

    Returns:
        No regresa nada, en cambios, las escribe en el archivo 'user_pass.txt' 
    """
    with open('user_pass.txt','w') as file:
        for contra in range(1):
            file.write("usuario {} {}\n".format(contra, desencripta_una(contra)))                  
    return "Terminamos :)" 

def contra_juanito():
    """ Encuentra la contraseña de Juanito

    Returns:
        bytes: contraseña desencriptada 
    """
    sal = bytes.fromhex("d8201aae236713fefe9a5266dc1f8012")
    contra_hash = bytes.fromhex("5f495364792782144918397bdbb72bc04326a883138a11f3d0b61a3d2576ca00")
    contrasenias = get_batch(1000)
    for i in contrasenias:         
        salida = hashlib.scrypt(i, salt=sal,n=2**16, r=8, p=1, maxmem=2**30, dklen=32)
        if salida == contra_hash:
            return i


if __name__ == "__main__":
    path = "./BD_jaqueada.txt"
    #Diccionario que almacena los datos de los usuarios
    users = lee_bd(path)
    # Contraseñas de la base de datos hackeada, ejercicio 2.1
    print(desencripta())
    # Contraseña de Juanito, ejercicio 2.2
    # print(contra_juanito())