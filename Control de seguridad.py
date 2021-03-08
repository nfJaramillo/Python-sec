from Crypto.Hash import MD5
from Crypto.Hash import SHA1
from Crypto.Hash import SHA256

def getDigestMD5( buffer ):
    h = MD5.new()
    h.update(buffer)
    print ("Digest MD5 obtenido: " + h.hexdigest())

def getDigestSHA1( buffer ):
    h = SHA1.new()
    h.update(buffer)
    print ("Digest SHA-1 obtenido: " +h.hexdigest())

def getDigestSHA256( buffer ):
    h = SHA256.new()
    h.update(buffer)
    print ("Digest SHA-256 obtenido: " +h.hexdigest())

def getDigestFileMD5(nombreArchivo):
    archivo = open(nombreArchivo, "r")
    archivo = archivo.read()

    getDigestMD5(archivo.encode())

def getDigestFileSHA1(nombreArchivo):
    archivo = open(nombreArchivo, "r")
    archivo = archivo.read()

    getDigestSHA1(archivo.encode())

def getDigestFileSHA256(nombreArchivo):
    archivo = open(nombreArchivo, "r")
    archivo = archivo.read()

    getDigestSHA256(archivo.encode())
    
mensaje = input("Escriba un mensaje de texto: ") 
print(mensaje) 
print ("Mensaje de entrada: " + mensaje)
getDigestMD5(mensaje.encode())
