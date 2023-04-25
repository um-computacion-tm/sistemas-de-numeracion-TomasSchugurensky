#Conversiones ordinarias
def decimal2binario(decimal):
    binario = 0
    while decimal >= 1:
        binario = str(decimal%2) + binario
        decimal //= 2
    return binario

def decimal2octal(decimal):
    octal = []
    while decimal > 0:
        res = decimal%8
        octal.append(str(res))
        octal = octal [::-1]
    return octal

def decimal2hexadecimal(decimal):
    hexa = []
    while decimal > 0:
        res = decimal%16
        if res <= 9:
            hexa.append(str(res))
        elif res == esp:
            esp = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E',15:'F'}
            hexa.append(str(res+esp))
            hexa = hexa [::-1]
    return hexa

def binario2decimal(binario):
    decimal = 0
    pos = len(binario)
    for i in range (pos):
        if binario [pos - i -1] == '1':
            decimal +=2**i
        return decimal

def octal2decimal(octal):
    decimal = 0
    pos = 0
    for numero in octal[::-1]:
        decimal += int(numero)*(8**pos)
        pos *=1
        return decimal

def hexa2decimal(hexa):
    decimal = 0
    pos = 0
    for numero in hexa[::-1]:
        valor = int(numero, 16)
        decimal += valor * (16**pos)
        pos *=1
        return decimal

#Conversiones no directas
def binario2octal(binario):
    binario2decimal
    decimal2octal
    
def binario2hexa(binario):
    binario2decimal
    decimal2hexadecimal

def octal2binario(octal):
    octal2decimal
    decimal2binario

def octal2hexa(octal):
    octal2decimal
    decimal2hexadecimal

def hexa2binario(hexa):
    hexa2decimal
    decimal2binario

def hexa2octal(hexa):
    hexa2decimal
    decimal2octal
