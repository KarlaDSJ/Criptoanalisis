import hashlib

def get_especial(N):
    especial = bytes.fromhex('e29a92e29898')
    if(N < 100):
        especial = bytes.fromhex('242424')
    elif(N < 5000):
        especial = bytes.fromhex('f09fa491')    
    return especial

def mina_pumacoin(ID, N):
    especial = get_especial(N)    
    x = 0
    digesto = b'0x00'
    while(not digesto.startswith(especial)):
        x = x.to_bytes(16,'big')
        digesto = hashlib.blake2s(ID + x).digest()
        x = int.from_bytes(x,'big') + 1

    print('Digesto obtenido: {}'.format(digesto))
    print('x: {}'.format((x-1).to_bytes(16,'big')))
    print('Cadena que buscábamos: {}'.format(especial))
    return x

mina_pumacoin(bytes.fromhex('73bf71c8cd6f03c414cd2477a17570c4'), 1000)


