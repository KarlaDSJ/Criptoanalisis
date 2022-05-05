import hashlib

def get_especial(N):
    """ Obtiene la cadena especial a buscar acorde al número de mineros

    Args:
        N (int): número de mineros

    Returns:
        bytes: cadena especial
    """
    especial = bytes.fromhex('e29a92e29898')
    if(N < 100):
        especial = bytes.fromhex('242424')
    elif(N < 5000):
        especial = bytes.fromhex('f09fa491')    
    return especial

def mina_pumacoin(ID, N):
    """ Encuentra una cadena tal que al concatenarla
    con el id del minero comience con una cadena especial
    determinada por el número de mineros que hay

    Args:
        ID (bytes): cadena de 16 bytes
        N (int): número de mineros

    Returns:
        bytes: cadena que se concatenó de 16 bytes
    """
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

# mina_pumacoin(bytes.fromhex('d1c5593465eb5bfb9fcad9adf90af61f'), 50)
# mina_pumacoin(bytes.fromhex('73bf71c8cd6f03c414cd2477a17570c4'), 1000)


