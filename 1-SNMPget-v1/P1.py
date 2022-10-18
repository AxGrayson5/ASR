from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from os import remove, path, rename, listdir
from pysnmp.hlapi import *
import itertools


alto, ancho = letter


def obtenerinfo(objectid, ip="localhost", puerto=161, comunidad="comunidadASR"):
    respuesta = ""
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(comunidad, mpModel=0),
        UdpTransportTarget((ip, puerto)),
        ContextData(),
        ObjectType(ObjectIdentity(objectid))
    )

    errorindication, errorstatus, errorindex, varbinds = next(iterator)

    if errorindication:
        print(errorindication)

    elif errorstatus:
        print('%s at %s' % (errorstatus.prettyPrint(),
                            errorindex and varbinds[int(errorindex) - 1][0] or '?'))

    else:
        for varBind in varbinds:
            respuesta = (' = '.join([x.prettyPrint() for x in varBind]))

    return respuesta


def hex_to_string(hexadecimal):
    new = ""
    if hexadecimal[:2] == '0x':
        new = hexadecimal[2:]
    string_value = bytes.fromhex(new).decode('utf-8')
    return string_value


def export_to_pdf(data, c):
    c.setFont("Times-Roman", 12)
    max_rows_per_page = 25
    # Margin.
    x_offset = 50
    y_offset = 50
    # Space between rows.
    padding = 25

    xlist = [x + x_offset for x in [0, 275, 275, 390]]
    ylist = [ancho - y_offset - i * padding for i in range(max_rows_per_page + 1)]

    for rows in grouper(data, max_rows_per_page):
        rows = tuple(filter(bool, rows))
        c.grid(xlist, ylist[:len(rows) + 1])
        for y, row in zip(ylist[:-1], rows):
            for x, cell in zip(xlist, row):
                if len(str(cell)) > 40:
                    c.drawString(x + 2, y - padding + 3, str(cell)[0:40] + "...")
                else:
                    c.drawString(x + 2, y - padding + 3, str(cell))
        c.showPage()

    c.save()


def grouper(iterable, n):
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args)


print('Sistema de administracion de Red')
print('Practica 1 - Adquisicion de informacion')
print('Hernandez Gonzalez Manuel Alexis  4CM16  2019630532')
print('1) Agregar dispositivo')
print('2) Cambiar informacion de dispositivo')
print('3) Eliminar dispositivo')
print('4) Generar reporte')
print('Elige una opcion:')

opcion = int(input())

if opcion == 1:
    print('Ingrese la comunidad:')
    comunidad = input()
    print('Ingrese la version SNMP:')
    version = input()
    print('Ingrese el puerto:')
    puerto = int(input())
    print('Ingrese la ip:')
    ip = input()
    Agregar = open(ip + "_" + str(puerto) + ".txt", "w+")
    Agregar.write(comunidad + "\n" + version + "\n" + str(puerto) + "\n" + ip)
    Agregar.close()
elif opcion == 2:
    print("Ingrese el IP y el puerto del dispositivo a modificar [127.0.0.1_80]:")
    dispositivo = input()
    Agregar = open(dispositivo + ".txt", "r+")
    Lectura = Agregar.read()
    Agregar.close()
    Lectura = Lectura.split("\n")
    print('Comunidad:'+Lectura[0])
    print('Version SNMP:'+Lectura[1])
    print('Puerto:'+Lectura[2])
    print('Ip:'+Lectura[3])
    print('Ingrese la comunidad:')
    comunidad = input()
    print('Ingrese la version SNMP:')
    version = input()
    print('Ingrese el puerto:')
    puerto = int(input())
    print('Ingrese la ip:')
    ip = input()
    rename(dispositivo + ".txt", ip + "_" + str(puerto) + ".txt")
    Agregar = open(ip + "_" + str(puerto) + ".txt", "w+")
    Agregar.write(comunidad + "\n" + version + "\n" + str(puerto) + "\n" + ip)
    Agregar.close()
elif opcion == 3:
    print("Ingrese el IP y el puerto del dispositivo a eliminar [127.0.0.1_80]:")
    dispositivo = input()
    remove(dispositivo + ".txt")
elif opcion == 4:
    Files = listdir("./")
    for file in Files:
        if path.isfile(path.join("./", file)) and file.lower().endswith(".txt"):
            print(file.title()[0:-4])
    print("Ingrese el IP y el puerto del dispositivo a generar reporte [127.0.0.1_80]:")
    dispositivo = input()
    Agregar = open(dispositivo + ".txt", "r+")
    Lectura = Agregar.read()
    Agregar.close()
    Lectura = Lectura.split("\n")
    c = canvas.Canvas("Practica1-AlexisHG.pdf", pagesize=letter)
    c.setTitle("Practica 1: SNMP")
    c.drawImage("IPN.png", 50,  alto + 25, width=100, height=100)
    c.drawImage("ESCOM.png", 480, alto + 25, width=100, height=100)
    c.setFont("Times-Roman", 18)
    c.drawCentredString(ancho / 2.5, alto + 100, "INSTITUTO POLITECNICO NACIONAL")
    c.setFont("Times-Roman", 16)
    c.drawCentredString(ancho / 2.5, alto, "ESCUELA SUPERIOR DE COMPUTO")
    c.setFont("Times-Roman", 14)
    c.drawCentredString(ancho / 2.5, alto - 100, "Administracion de Servicios en Red")
    c.setFont("Times-Roman", 12)
    c.drawCentredString(ancho / 2.5, alto - 200, "Practica 1: Adquisicion de informacion usando SNMP")
    c.drawCentredString(ancho / 2.5, alto - 300, "Tanibet Perez de los Santos")
    c.drawCentredString(ancho / 2.5, alto - 400, "Hernandez Gonzalez Manuel Alexis")
    c.showPage()
    res = obtenerinfo('1.3.6.1.2.1.1.1.0', Lectura[3], int(Lectura[2]), Lectura[0])
    sysOp = res.split(" = ")[1].split(": ")[2]
    res = obtenerinfo('1.3.6.1.2.1.1.4.0', Lectura[3], int(Lectura[2]), Lectura[0])
    contact = res.split(" = ")[1]
    res = obtenerinfo('1.3.6.1.2.1.1.5.0', Lectura[3], int(Lectura[2]), Lectura[0])
    eqName = res.split(" = ")[1]
    res = obtenerinfo('1.3.6.1.2.1.1.6.0', Lectura[3], int(Lectura[2]), Lectura[0])
    comunity = res.split(" = ")[1]

    c.setFont("Times-Roman", 12)
    c.drawCentredString((ancho / 2.5) - 50, alto + 100, "Sistema operativo: " + sysOp)
    if sysOp.__contains__("Windows"):
        c.drawImage("Windows.png", (ancho / 2.5) + 150, alto + 100, width=50, height=50)
    if sysOp.__contains__("Linux"):
        c.drawImage("Linux.png", (ancho / 2.5) + 150, alto + 100, width=50, height=50)
    if sysOp.__contains__("Mac"):
        c.drawImage("Mac.png", (ancho / 2.5) + 150, alto + 100, width=50, height=50)

    c.drawCentredString(ancho / 2.5, alto, "Contacto: " + contact)
    c.drawCentredString(ancho / 2.5, alto - 100, "Nombre equipo: " + eqName)
    c.drawCentredString(ancho / 2.5, alto - 200, "Ubicacion: " + comunity)
    Tabla = [("interfaz", "estado administrativo")]
    interfaces = obtenerinfo("1.3.6.1.2.1.2.1.0", Lectura[3], int(Lectura[2]), Lectura[0])
    interfaces = interfaces.split(" = ")[1]
    c.drawCentredString(ancho / 2.5, alto - 300, "#Interfaces: " + interfaces)
    c.showPage()
    for i in range(1, int(interfaces)):
        interfaz = obtenerinfo("1.3.6.1.2.1.2.2.1.2."+str(i), Lectura[3], int(Lectura[2]), Lectura[0])
        interfaz = interfaz.split(" = ")[1]
        interfaz = hex_to_string(interfaz)
        estado = obtenerinfo("1.3.6.1.2.1.2.2.1.7."+str(i), Lectura[3], int(Lectura[2]), Lectura[0])
        estado = estado.split(" = ")[1]
        if estado == "1":
            estado = "up"
        elif estado == "2":
            estado = "down"
        else:
            estado = "testing"
        Tabla.append((interfaz, estado))
    export_to_pdf(Tabla, c)
