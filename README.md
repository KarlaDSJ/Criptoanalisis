# Criptoanálisis

## Ejercicio 1 

Para encriptar
```
cd ejercicio1/Mis archivos
python3 juego.py
```

Para desencriptar
```
cd ejercicio1
python3 desencripta.py
```

## Ejercicio 2

Para correrlo:
```
cd ejercicio2
python3 ejercicio2.py
```

Las contraseñas de cada usuario se encuentran en ejercicio2/user_pass.txt


Contaseña de juanito 

```
WqàñFCAdv¨p¡À
i"'h®¤ìÈÛÀÇÙÍmxÅÚÎnºéñG©9áAEÉÌ
                              <`
v
```

## Ejercicio 3
Dado el identificador de un bloque de transacciones id, de longitud 16 bytes, los mineros tienen el reto de encontrar una cadena x de 16 bytes tal que el digesto generado por BLAKE2s-256(id||x) tiene al principio una cadena de bytes especial.

###  50 mineros
Cadena especial para cuando hay a lo más 100 mineros = 0x242424.

```
id = 'd1c5593465eb5bfb9fcad9adf90af61f'
x = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00)w\xbc'
BLAKE2s-256(id || x) = b'$$$\x96G\x1cs(\xb2\x8b\xfc\xc2\xae\xa9\xb1\x1b\xbfB\xd4\xa6\x98\x9fw\x8a4\x070\t\x8a\x08\x02I'
```

### 1000 mineros 
Cadena especial cuando 100 < núm. de mineros < 5000 = 0xf09fa491.

```
id = '0x73bf71c8cd6f03c414cd2477a17570c4'
x = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x80Q\x9a}'
BLAKE2s-256(id || x) = b"\xf0\x9f\xa4\x91\xad\xa2\x9bgr\xb4\xba\xd7N\xbf\x81\xa1\x18aF@\xe3\xdc'\xb1\xdc\xff\xac\xb4\xa6\xc5*Q"
```

## Ejercicio 4

Para correrlo
```
python3 ejercicio4.py
```