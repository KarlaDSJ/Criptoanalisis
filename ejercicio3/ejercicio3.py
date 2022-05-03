import hashlib

def get_especial(N):
    especial = 'e29a92e29898'
    
    if(N < 100):
        especial = '242424'
    elif(N < 5000):
        especial = 'f09fa491'
    
    return especial

def mina_pumacoin(ID, N):
    especial = get_especial(N)
    
    x = 0
    digesto = b'0x00'
    while(not digesto.startswith(especial)):
        x = x.to_bytes(16,'big')
        digesto = hashlib.blake2s(ID + x).hexdigest()
        x = int.from_bytes(x,'big') + 1
    print('Digesto: {}'.format(digesto))
    print('x: {}'.format(x))
    # print("---------------------------------")
    # print("\n")
    print('Cadena que buscábamos: {}'.format(especial))
    print('Digesto inicia con la cadena que buscábamos: {}'.format(digesto.startswith(especial)))
    return x

# (0xd1c5593465eb5bfb9fcad9adf90af61f, 50)
# 0x73bf71c8cd6f03c414cd2477a17570c4, 1000
# mina_pumacoin(bytes.fromhex('d1c5593465eb5bfb9fcad9adf90af61f'), 50)
# x = b'\xba\x82\xa9|\x1eN\xfd\xe3\x84\x11 %\x8aM\xbf\xfd'
mina_pumacoin(bytes.fromhex('0x73bf71c8cd6f03c414cd2477a17570c4'), 1000)


