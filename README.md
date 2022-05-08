# Criptoanálisis

## Equipo de trabajo:
- Kethrim, [*Kethrim*](https://github.com/Kethrim)
- Miguel, [*josemigueltr*](https://github.com/josemigueltr)
- Ariana, [*arianafm*](https://github.com/arianafm)
- Karla, [*KarlaDSJ*](https://github.com/KarlaDSJ)

<a id="ejercicio"></a>
## Ejercicios:
1. [**Vacuna para ransomware**](#ejercicio-1)
   
2. [**Contraseñas en bases de datos**](#ejercicio-2)

3. [**Minando pumacoins**](#ejercicio-3)

4. [**Implementando modos de operación**](#ejercicio-4)
___


<a id="ejercicio-1"></a>
## Vacuna para ransomware  <small>[[Top](#ejercicio)]</small>

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

Para este ejercicio hicimos un análisis del archivo "juego.py", en donde notamos
que a cada archivo se le aplicaba un xor con una cadena de 16 bytes llamada k. Ésta 
k se guarda en un archivo oculto, claro, encriptada. 

Para poder desencriptar abrimos el archivo oculto y separamos los 65 bytes en 3:
- c : es un byte que nos ayuda a denecriptar la k
- d : cadena de 16 bytes que ayuda a denecriptar la k
- k encriptada : cadena de 16 bytes encriptada

E hicimos el proceso inverso para encriptar la k:
    Encriptar: k_encriptada = d*k%(1<<c)
    Desencriptar : k = (k__encriptada * modinv(d, 1<<c) ) % (1<<c)

donde modinv(a, m) indica el inverso multiplicativo de a módulo m
Finalmente aplicamos el xor como en el archivo juego.py a cada archivo encriptado. 

<a id="ejercicio-2"></a>
## Contraseñas en bases de datos  <small>[[Top](#ejercicio)]</small>

Para correrlo:
```
cd ejercicio2
python3 ejercicio2.py
```

Las contraseñas de cada usuario se encuentran en ejercicio2/user_pass.txt

Este ejercicio fue realizado por fuerza bruta, pero tomando algunas consideraciones, debido a que el archivo de contraseñas es muy grande no sería posible cargarlo todo a memoria, alguna computadora podría morir, por ese motivo lo que hacemos es irlo leyendo por bloques, por cada contraseña requerimos de esos bloques de datos y por cada dato probamos `$salt$sha256(contraseña||salt)` o `$salt$sha256(salt||contraseña)`, paramos cuando encontramos la contraseña dejamos de solicitar bloques y guardamos en un archivo la contraseña en texto claro.

### Contaseña de juanito 

No pudimos encontrarla ya que el hecho de que usemos el algoritmo de scrypt con los 
parámetros que se nos dan hace que sea mucho más tardado encriptar. 

FALTA agregar un estimado del tiempo para que nos la de 


<a id="ejercicio-3"></a>
## Minando pumacoins  <small>[[Top](#ejercicio)]</small>

Dado el identificador de un bloque de transacciones id, de longitud 16 bytes, los mineros tienen el reto de encontrar una cadena x de 16 bytes tal que el digesto generado por BLAKE2s-256(id||x) tiene al principio una cadena de bytes especial.

Para correrlo
```
python3 ejercicio3.py
```
Este ejercicio al igual que el anterior se hace por fuerza bruta, dado que tenemos el principio de la cadena que buscamos lo que hacemos es iniciar con una cadena aleatoria de 16 bytes, en cada iteración le sumamos uno a esta cadena y aplicamos `BLAKE2s-256(id||x)` hasta que el inicio de la cadena es igual a la cadena de acuerdo a los mineros participantes.

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

<a id="ejercicio-4"></a>
## Implementando modos de operación  <small>[[Top](#ejercicio)]</small>
Se implementan las funciones de cifrado y descifrado de los modos CBC y CTR usando AES con llaves de 128 bits, utilizando el modo ECB como base para poder aplicar $AES_k$ o $AES_k^{-1}$

Para correrlo
```
python3 ejercicio4.py
```



