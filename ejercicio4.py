from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import ECB
import os

def relleno(mensaje):
    cant_relleno = 16- len(mensaje) % 16
    relleno = hex(cant_relleno)
    aux = hex(cant_relleno).lstrip("0x")
    if len(aux)<2:
        aux = "0"+ aux
    aux = aux*cant_relleno
    relleno = bytes.fromhex(aux)
    return relleno

def quita_relleno(bloque):
    cant = bloque[-1]
    return bloque[:(16-cant)] 


def aes128_cbc_enc(llave, mensaje):    
    rell = relleno(mensaje)
    cuatro = os.urandom(16)
    texto_plano = mensaje+rell 
    bloques = [texto_plano[i:i + 16] for i in range(0, len(texto_plano), 16)]
    c = [cuatro]
    i = 0
    for bloque in bloques:
        aes = Cipher(AES(llave), ECB())
        enc = aes.encryptor()
        resultado = int.from_bytes(bloque, byteorder="big") ^ int.from_bytes(c[i], byteorder="big")
        texto_encriptar = resultado.to_bytes(16, byteorder="big")
        c.append(enc.update(texto_encriptar)+enc.finalize())
        i +=1
    
    texto_cifrado = b''
    for cifrado in c:

        texto_cifrado += cifrado
        
    return texto_cifrado

def aes128_cbc_dec(llave, cifrado):
    bloques = [cifrado[i:i + 16] for i in range(0, len(cifrado), 16)]
    c = b''
    for i in range(1,len(bloques)):
        aes_k = Cipher(AES(llave), ECB())
        dec = aes_k.decryptor()
        desencriptado = dec.update(bloques[i]) + dec.finalize()
        desencriptado = int.from_bytes(bloques[i-1], byteorder="big") ^ int.from_bytes(desencriptado, byteorder="big")
        desencriptado = desencriptado.to_bytes(16, byteorder="big")
        if i == len(bloques)-1:
            desencriptado = quita_relleno(desencriptado)
        c += desencriptado
    return c
    
def aes128_ctr_enc(llave, mensaje):
    rell = relleno(mensaje)
    cuatro = os.urandom(8)
    texto_plano = mensaje+rell 
    contador = 0
    bloques = [texto_plano[i:i + 16] for i in range(0, len(texto_plano), 16)]
    c = cuatro
    for bloque in bloques:
        aes = Cipher(AES(llave), ECB())
        enc = aes.encryptor()
        cifrado = enc.update(cuatro+contador.to_bytes(8, byteorder="big"))+enc.finalize()
        resultado = int.from_bytes(bloque, byteorder="big") ^ int.from_bytes(cifrado, byteorder="big")        
        texto_encriptar = resultado.to_bytes(length=16, byteorder="big")
        c+=texto_encriptar
        contador +=1
    return c
    
    
def aes128_ctr_dec(llave, cifrado):
    print(len(cifrado))
    bloques = [cifrado[i:i + 16] for i in range(8, len(cifrado), 16)]
    cuatro = cifrado[:8]
    c = b''
    for i in range(len(bloques)):
        aes_k = Cipher(AES(llave), ECB())
        dec = aes_k.encryptor()
        desencriptado = dec.update(cuatro+i.to_bytes(8, byteorder="big")) + dec.finalize()
        desencriptado = int.from_bytes(desencriptado, byteorder="big") ^ int.from_bytes(bloques[i], byteorder="big")
        desencriptado = desencriptado.to_bytes(length=16, byteorder="big")
        if i == len(bloques)-1:
            desencriptado = quita_relleno(desencriptado)
        c += desencriptado
    return c

# Para hacer pruebas
llave = b'Mi llave secreta'
mensaje = b'Mensaje de texto mas grande que un bloque y de longitud que si es multiplo de 16'
mensaje2 = b'UwU'

"""print("---------------CBC--------------------")
print("Mensaje 1: ", mensaje)
texto_enc = aes128_cbc_enc(llave, mensaje)
print("Texto cifrado: ", texto_enc)

texto_claro = aes128_cbc_dec(llave, texto_enc)
print("Mensaje original: ", texto_claro)

print("Mensaje 2: ", mensaje2)
texto_enc = aes128_cbc_enc(llave, mensaje2)
print("Texto cifrado: ", texto_enc)

texto_claro = aes128_cbc_dec(llave, texto_enc)
print("Mensaje original: ", texto_claro)"""

print("---------------CTR--------------------")
print("Mensaje 1: ", mensaje)
texto_enc = aes128_ctr_enc(llave, mensaje)
print("Texto cifrado: ", texto_enc)

texto_claro = aes128_ctr_dec(llave, texto_enc)
print("Mensaje original: ", texto_claro)

print("Mensaje 2: ", mensaje2)
texto_enc =aes128_ctr_enc(llave, mensaje2)
print("Texto cifrado: ", texto_enc)

texto_claro = aes128_ctr_dec(llave, texto_enc)
print("Mensaje original: ", texto_claro)
