import hashlib

def encuentra_contra(sal, contra_hash, contras):
    for i in contras:        
        aux = sal+i
        aux2 = i+sal
        salida1 = hashlib.sha256(aux).digest()
        salida2 = hashlib.sha256(aux2).digest()
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
    gen = get_batch(1000)
    for batch in gen:
        x = encuentra_contra(users[id][0], users[id][1], batch)
        if x != None:
            return x
    print("no respuesta")

def desencripta():
    with open('user_pass.txt','w') as file:
        for contra in range(len(users)):
            file.write("usuario {} {}\n".format(contra, desencripta_una(contra)))            
    return "Terminamos :)" 


path = "./BD_jaqueada.txt"
#Diccionario que almacena los datos de los usuarios
users = []
with open(path) as f:
    for line in f:
        info = line.split('$')
        #0 - usuario, 1 - salt, 2- hash
        try:
            last = (bytes.fromhex(info[1]), bytes.fromhex(info[2][:-1]))
        except ValueError:
            continue
        users.append(last)

print(desencripta())
# Contraseña de Juanito, ejercicio 2.2
# contra_hash = bytes.fromhex('5f495364792782144918397bdbb72bc04326a883138a11f3d0b61a3d2576ca00')
# contra = hashlib.scrypt(contra_hash, salt=bytes.fromhex('d8201aae236713fefe9a5266dc1f8012'), n=2*16, r=8, p=1, maxmem=2*30 )
# print(contra.decode("latin1"))