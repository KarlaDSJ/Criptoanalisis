import hashlib
import threading

path = "./BD_jaqueada.txt"
#Diccionario que almacena los datos de los usuarios
users = []
with open(path) as f:
    for line in f:
        info = line.split('$')
        #0 - usuario, 1 - salt, 2- hash
        users.append((info[1], info[2]))


def encuentra_contra(sal, contra_hash, contras):
    for i in contras:
        aux = sal+i
        aux2 = i+sal
        # probar con blake2s
        salida1 = hashlib.blake2s(aux.encode('latin1')).hexdigest()
        salida2 = hashlib.blake2s(aux2.encode('latin1')).hexdigest()
        if salida1 == contra_hash or salida2 == contra_hash:
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
            break
    print("no respuesta")

def desencripta():
    resp = []
    for id in range(10):
        resp.append(desencripta_una(id))
    return resp 

#desencripta()

# Clase hilo
class MiHilo(threading.Thread):
    def init(self,x):
        self.x = x
        threading.Thread.__init(self)

    def run (self):  # run() se utiliza para definir el comportamiento del hilo
        resp = []
        #for id in range(self.__x,self.__x):
        resp.append((self.__x,desencripta_una(self.__x)))
        print(resp)

# Inicia 10 hilos .hjhj
resp = []
for i in range(10):
    h=MiHilo(i)
    h.start() 
resp