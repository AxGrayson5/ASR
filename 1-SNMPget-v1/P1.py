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


print('Sistema de administracion de Red')
print('Practica 1 - Adquisicion de informacion')
print('Hernandez Gonzalez Manuel Alexis  4CM16  2019630532')
print('1) Agregar dispositivo')
print('2) Cambiar informacion de dispositivo')
print('3) Eliminar dispositivo')
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
