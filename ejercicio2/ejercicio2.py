import hashlib
import threading

path = "./BD_jaqueada.txt"
#Diccionario que almacena los datos de los usuarios
users = []
with open(path) as f:
    for line in f:
        info = line.split('$')
        #0 - usuario, 1 - salt, 2- hash
        users.append((info[1], int(info[2], 16)))

def encuentra_contra(sal, contra_hash, contras):
    for i in contras:        
        aux = sal+i
        aux2 = i+sal
        salida1 = int(hashlib.sha3_256(aux.encode('latin1')).hexdigest(), 16)
        salida2 = int(hashlib.sha3_256(aux2.encode('latin1')).hexdigest(), 16)
        if salida1 & contra_hash or salida2 & contra_hash:
            return i

def get_batch(batchSize):
    # Lista de diccionarios que representará el batch de documentos.        
    batch = []
    # Líneas procesadas hasta el momento.
    processedLines = 0
    # Id del batch actual.
    idBatch = 0
    with open("passwords.txt", encoding='latin1') as infile:
        for line in infile:            
            batch.append(line)
            processedLines += 1
            if processedLines == batchSize:
                processedLines = 0
                yield batch
                batch = []
        if processedLines < batchSize:
            yield batch

def desencripta_una(id):
    gen = get_batch(10000)
    for batch in gen:
        x = encuentra_contra(users[id][0], users[id][1], batch)
        if x != None:
            return x
    print("no respuesta")

def desencripta():
    with open('user_pass.txt','w') as file:
        for id in range(len(users)):
            file.write("usuario {} {}\n".format(id,desencripta_una(id).encode('latin-1')))            
    return "Terminamos :)" 

print(desencripta())