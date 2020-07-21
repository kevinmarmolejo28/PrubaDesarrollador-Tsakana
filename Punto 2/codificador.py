from string import ascii_uppercase

ascii_uppercase
alf0 = []
alf1 = []
size = len(ascii_uppercase)

for i in range(size):
    alf0.append(ascii_uppercase[i])
    alf1.append(ascii_uppercase[i])

alf0.insert(14, 'Ñ')
alf1.insert(14, 'Ñ')
alf0.append(' ')

############## Estos metodos toman en cuenta el espacio #####################
def codificar0(msj, num):
    result = ''
    size = len(msj)

    for i in range(size):
        letra = msj[i]        
        pos = alf0.index(letra)
        newPos = pos + num        
        if newPos > 27:
            newPos = newPos - 28
        result = result + alf0[newPos]     
    return result

def decodificar0(msj, num):
    result = ''
    size = len(msj)

    for i in range(size):
        letra = msj[i]        
        pos = alf0.index(letra)
        newPos = pos - num   
        if newPos > 27:
            newPos = newPos - 28 
        result = result + alf0[newPos]     
    return result

############## Estos metodos no toman en cuenta el espacio #####################
def codificar1(msj, num):
    result = ''
    size = len(msj)

    for i in range(size):
        letra = msj[i]        
        pos = alf1.index(letra)
        newPos = pos + num        
        if newPos > 26:
            newPos = newPos - 27
        result = result + alf1[newPos]     
    return result

def decodificar1(msj, num):
    result = ''
    size = len(msj)

    for i in range(size):
        letra = msj[i]        
        pos = alf1.index(letra)
        newPos = pos - num   
        if newPos > 26:
            newPos = newPos - 27 
        result = result + alf1[newPos]     
    return result

############## Pruebas con espacio #####################
mensaje0 = "ABC "
mensajeCodificado0 = codificar0(mensaje0, -1)
mensajeDecodificado0 = decodificar0(mensajeCodificado0, -1)

print("----------- PRUEBA 1 -----------")
print(mensaje0)
print(mensajeCodificado0)
print(mensajeDecodificado0)

############## Pruebas sin espacio #####################
print("----------- PRUEBA 2 -----------")
mensaje1 = "ABC"
mensajeCodificado1 = codificar1(mensaje1, -1)
mensajeDecodificado1 = decodificar1(mensajeCodificado1, -1)

print(mensaje1)
print(mensajeCodificado1)
print(mensajeDecodificado1)