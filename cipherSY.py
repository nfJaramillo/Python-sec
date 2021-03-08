from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64, os
import time

def generarLlaveAES():
    # Para AES-128 generamos una llave de 16 bytes
    tamanoLlave = 16
    llave = os.urandom(tamanoLlave)
    return llave

def cifrar(llave, mensaje):
    textoClaro = mensaje.encode()
    print ("Texto claro: " + imprimir (textoClaro))
    iv = 16 * b'\x00'
    cipher = AES.new(llave, AES.MODE_CBC, iv)
    textoCifrado = cipher.encrypt(pad(textoClaro,AES.block_size))
    return textoCifrado

def descifrar(llave, textoCifrado):
    iv = 16 * b'\x00'
    cipher = AES.new(llave, AES.MODE_CBC,iv)
    textoClaro = unpad(cipher.decrypt(textoCifrado), AES.block_size)
    print ("Texto descifrado: " + imprimir (textoClaro))
    mensaje = textoClaro.decode()
    return mensaje

def imprimir (texto):
    resp = ""
    for x in texto:
        resp += (str(x) + " ")
    return(resp)

    

### empeiza


mensaje = input("Escriba el texto que desea cifrar: ") 
print(mensaje) 
print ("Mensaje de entrada en texto claro: " + mensaje)

tiempoInicial = time.time()
llave = generarLlaveAES()

mensajeCifrado = cifrar(llave,mensaje)
print ("Texto cifrado: " + imprimir (mensajeCifrado))
mensajeDescifrado = descifrar(llave,mensajeCifrado)
print ("Texto descifrado: " + mensajeDescifrado)
tiempoFinal = time.time()

tiempo = tiempoFinal - tiempoInicial

print (tiempo)

#print ("PARTE 2 ------")

#archivo = open("nombreArchivo.txt", "wb")
#archivo.write(llave.export_key())
#archivo.close()

#archivo = open("nombreArchivo.txt", "wb")
#archivo.write(textoCifrado)
#archivo.close()


#archivo = open("nombreArchivo.txt", "rb")
#archivo = RSA.import_key(archivo.read())

#archivo = open("nombreArchivo.txt", "rb")
#archivo = archivo.read()


#print (descifrar(fa,fb))



    
    
    
    
