import hashlib

def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

def mina_pumacoin(ID, N):
    if(N < 100):
        prefix = '242424'
    elif(N < 5000):
        prefix = 'f09fa491'
    else:
        prefix = 'e29a92e29898'
    proof = 0
    id = ID.encode()
    x = get_new_x(id, proof)
    while(not x.startswith(prefix)):
        proof +=1
        x = get_new_x(id, proof)
    return proof.to_bytes(16,'big')

def get_new_x(id, seed):
    x = hashlib.blake2s(id + seed.to_bytes(16, 'big')).hexdigest()
    return x

print(mina_pumacoin('0x73bf71c8cd6f03c414cd2477a17570c4', 1000))