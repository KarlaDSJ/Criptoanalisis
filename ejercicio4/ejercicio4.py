from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import ECB

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
    x = mensaje % 16

def aes128_cbc_dec(llave, cifrado):
    # FALTA IMPLEMENTAR
    pass
    
def aes128_ctr_enc(llave, mensaje):
    # FALTA IMPLEMENTAR
    pass
    
def aes128_ctr_dec(llave, cifrado):
    # FALTA IMPLEMENTAR
    pass

    