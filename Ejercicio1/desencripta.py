from sys import argv
import os

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

#Inverso multiplicativo de un modulo con modulo
def modinv(a, m):
    """ Encuentra el inverso multiplicativo de un número a 
    usando módulo m

    Args:
        a (int): número del que se desea encontrar su inverso multiplicativo
        m (int): módulo

    Raises:
        Exception: Si el inverso no existe

    Returns:
        int: inverso multiplicativo
    """
    # es x tal que a*x = 1 (mod m)
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
    
  
def obtener_k():
    """ Obtiene los 16 bytes aleatorios que se usaron para cifrar los archivos

    Returns:
        bytes: cadena de 16 bytes usada
    """
    with open('Mis archivos/.xyz','rb') as file:
        txt = file.read()
        c = txt[0]
        d = txt[1:33]
        k_new = txt[34:65]
        d = int.from_bytes(d,'big')
        k_new = int.from_bytes(k_new,'big')
        k = (k_new * modinv(d, 1<<c) ) % (1<<c)
        k = k.to_bytes(16,'big')
        # print(k)
        return k
    
def xx(x, k):
    """ Descifra un archivos, elimina el cifrado. Todo en la carpeta de Mis archivos

    Args:
        x (string): nombre del archivo encriptado
        k (bytes): cadena para descifrar
    """
    x = "Mis archivos/" + x
    file = x[:-4]
    with open(file,'wb') as z:
        z.write((lambda x:bytes([x[i]^k[i%16] for i in range(len(x))])) (open(x,'rb').read()))
        os.remove(x)   
        
       
if __name__ == '__main__':        
    _,_,x = next(os.walk('./Mis archivos'))
    try:
        x.remove('juego.py')    
    except Exception:
        pass
    k = obtener_k()
    x.remove('.xyz')
    list(map(lambda y: xx(y,k),x))
    os.remove('Mis archivos/.xyz') 