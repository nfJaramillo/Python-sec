from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import time


def generarLlaveRSA( ):
    llave = RSA.generate(1024)
    return llave
    

def cifrar(llave, mensaje):
    textoClaro = mensaje.encode()
    print ("Texto claro: " + imprimir (textoClaro))
    cipherRSA = PKCS1_OAEP.new(llave)
    textoCifrado = cipherRSA.encrypt(textoClaro)
    return textoCifrado

def descifrar(llave, textoCifrado):
    cipherRSA = PKCS1_OAEP.new(llave)
    textoClaro = cipherRSA.decrypt(textoCifrado)
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

llaves = generarLlaveRSA()
llavePrivada = llaves
llavePublica = llaves.publickey()

mensajeCifrado = cifrar(llavePublica,mensaje)
print ("Texto cifrado: " + imprimir (mensajeCifrado))
mensajeDescifrado = descifrar(llavePrivada,mensajeCifrado)
print ("Texto descifrado: " + mensajeDescifrado)
tiempoFinal = time.time()

tiempo = tiempoFinal - tiempoInicial

print (tiempo)



#print ("PARTE 2 ------")

#archivo = open("nombreArchivo.txt", "wb")
#archivo.write(llave)
#archivo.close()

#archivo = open("nombreArchivo.txt", "wb")
#archivo.write(textoCifrado)
#archivo.close()


#archivo = open("nombreArchivo.txt", "rb")
#archivo = archivo.read()

#arcvhivo = open("nombreArchivo.txt", "rb")
#arcvhivo = arcvhivo.read()


#print (descifrar(fa,fb))



    
    
    
    
