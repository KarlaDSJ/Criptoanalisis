from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import ECB
import os

def relleno(mensaje):
    cant_relleno = 16 - len(mensaje) % 16
    relleno = hex(cant_relleno)
    aux = hex(cant_relleno).lstrip("0x")
    if len(aux)<2:
        aux = "0"+ aux
    aux = aux*cant_relleno
    relleno = "0x"+ aux
    return relleno


def aes128_cbc_enc(llave, mensaje):
    aes = Cipher(AES(key), ECB())
    enc = aes.encryptor()
    # FALTA IMPLEMENTAR
    rell = relleno(mensaje)
    rell = bytes.fromhex(rell)
    mensaje = mensaje.encode()
    cuatro = os.urandom(16)
    texto_plano = mensaje+rell 
    bloques = [texto_plano[i:i + 16] for i in range(0, len(texto_plano), 16)]
    
    c = [cuatro]
    i = 0
    aes = Cipher(AES(llave), ECB())
    enc = aes.encryptor()
    for bloque in bloques:
        # c.append(bloque ^ c[i])
        resultado = int.from_bytes(bloque, byteorder="big") ^ int.from_bytes(c[i], byteorder="big")
        texto_encriptar = resultado.to_bytes(16, byteorder="big")
        c.append(enc.update(texto_encriptar))
        i +=1
    
    texto_cifrado = b''
    for cifrado in c:
        texto_cifrado += cifrado
        
    return texto_cifrado

def aes128_cbc_dec(llave, cifrado):
    # FALTA IMPLEMENTAR
    pass
    
def aes128_ctr_enc(llave, mensaje):
    # FALTA IMPLEMENTAR
    pass
    
def aes128_ctr_dec(llave, cifrado):
    # FALTA IMPLEMENTAR
    pass

    