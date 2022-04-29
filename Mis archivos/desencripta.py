def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    # es x tal que a*x = 1 (mod m)
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
    
    
def obtener_k():
    with open(".xyz",'rb') as file:
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
    
    
print(obtener_k())