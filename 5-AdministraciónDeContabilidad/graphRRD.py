import sys
import rrdtool
import time
tiempo_actual = int(time.time())
#Grafica desde el tiempo actual menos diez minutos
tiempo_inicial = tiempo_actual - 1800

"""ret = rrdtool.graphv( "segmentosTCP.png",
                     "--start",str(tiempo_inicial),
                     "--end","N",
                     "--vertical-label=Segmentos",
                     "--title=Segmentos TCP de un agente \n Usando SNMP y RRDtools",
                     "DEF:sEntrada=segmentosRed.rrd:segmentosEntrada:AVERAGE",
                     "DEF:sSalida=segmentosRed.rrd:segmentosSalida:AVERAGE",
                      "VDEF:segEntradaLast=sEntrada,LAST",
                      "VDEF:segEntradaFirst=sEntrada,FIRST",
                      "VDEF:segEntradaMax=sEntrada,MAXIMUM",
                      "VDEF:segEntradaDev=sEntrada,STDEV",
                      "CDEF:Nivel1=sEntrada,7,GT,0,sEntrada,IF",
                      "PRINT:segEntradaLast:%6.2lf",
                      "PRINT:segEntradaFirst:%6.2lf",
                     "GPRINT:segEntradaMax:%6.2lf %S segEntMAX",
                     "GPRINT:segEntradaDev:%6.2lf %S STDEV",
                     "LINE3:sEntrada#FF0000:Segmentros recibidos",
                     "LINE3:sSalida#0000FF:Segmentos enviados" )
print(ret)"""

ret = rrdtool.graphv( "Multicast.png",
                     "--start", str(tiempo_inicial),
                     "--end", "N",
                     "--vertical-label=Segmentos",
                     "--title=Paquetes multicast que ha enviado la interfaz de la interfaz de red de un agente \n Usando SNMP y RRDtools",
                     "DEF:multicast=segmentosRed.rrd:multicastOut:AVERAGE",
                     "VDEF:multicastLast=multicast,LAST",
                     "VDEF:multicastFirst=multicast,FIRST",
                     "VDEF:multicastMax=multicast,MAXIMUM",
                     "VDEF:multicastDev=multicast,STDEV",
                     "CDEF:Nivel1=multicast,7,GT,0,multicast,IF",
                     "PRINT:multicastLast:%6.2lf",
                     "PRINT:multicastFirst:%6.2lf",
                     "GPRINT:multicastMax:%6.2lf %S segEntMAX",
                     "GPRINT:multicastDev:%6.2lf %S STDEV",
                     "LINE3:multicast#FF0000:Paquetes multicast enviados")
print(ret)

ret = rrdtool.graphv( "Paquetes.png",
                     "--start", str(tiempo_inicial),
                     "--end", "N",
                     "--vertical-label=Segmentos",
                     "--title=Paquetes IP que los protocolos locales (incluyendo ICMP) suministraron a IP en las solicitudes de transmisión \n Usando SNMP y RRDtools",
                     "DEF:paquetes=segmentosRed.rrd:paquetesIp:AVERAGE",
                     "VDEF:paquetesLast=paquetes,LAST",
                     "VDEF:paquetesFirst=paquetes,FIRST",
                     "VDEF:paquetesMax=paquetes,MAXIMUM",
                     "VDEF:paquetesDev=paquetes,STDEV",
                     "CDEF:Nivel1=paquetes,7,GT,0,paquetes,IF",
                     "PRINT:paquetesLast:%6.2lf",
                     "PRINT:paquetesFirst:%6.2lf",
                     "GPRINT:paquetesMax:%6.2lf %S segEntMAX",
                     "GPRINT:paquetesDev:%6.2lf %S STDEV",
                     "LINE3:paquetes#339CFF:Paquetes IP")
print(ret)

ret = rrdtool.graphv( "ICMP.png",
                     "--start", str(tiempo_inicial),
                     "--end", "N",
                     "--vertical-label=Segmentos",
                     "--title=Mensajes ICMP que ha recibido el agente \n Usando SNMP y RRDtools",
                     "DEF:icmp=segmentosRed.rrd:ICMP:AVERAGE",
                     "VDEF:icmpLast=icmp,LAST",
                     "VDEF:icmpFirst=icmp,FIRST",
                     "VDEF:icmpMax=icmp,MAXIMUM",
                     "VDEF:icmpDev=icmp,STDEV",
                     "CDEF:Nivel1=icmp,7,GT,0,icmp,IF",
                     "PRINT:icmpLast:%6.2lf",
                     "PRINT:icmpFirst:%6.2lf",
                     "GPRINT:icmpMax:%6.2lf %S segEntMAX",
                     "GPRINT:icmpDev:%6.2lf %S STDEV",
                     "LINE3:icmp#6BFF33:Mensajes ICMP")

print(ret)

ret = rrdtool.graphv( "segments.png",
                     "--start", str(tiempo_inicial),
                     "--end", "N",
                     "--vertical-label=Segmentos",
                     "--title=El número de segmentos TCP transmitidos que contienen uno o más octetos transmitidos previamente \n Usando SNMP y RRDtools",
                     "DEF:segments=segmentosRed.rrd:segmentos:AVERAGE",
                     "VDEF:segmentsLast=segments,LAST",
                     "VDEF:segmentsFirst=segments,FIRST",
                     "VDEF:segmentsMax=segments,MAXIMUM",
                     "VDEF:segmentsDev=segments,STDEV",
                     "CDEF:Nivel1=segments,7,GT,0,segments,IF",
                     "PRINT:segmentsLast:%6.2lf",
                     "PRINT:segmentsFirst:%6.2lf",
                     "GPRINT:segmentsMax:%6.2lf %S segEntMAX",
                     "GPRINT:segmentsDev:%6.2lf %S STDEV",
                     "LINE3:segments#FFFF33:Segmentos retransmitidos")

print(ret)

ret = rrdtool.graphv( "Datagramas.png",
                     "--start", str(tiempo_inicial),
                     "--end", "N",
                     "--vertical-label=Segmentos",
                     "--title=Datagramas enviados por el dispositivo \n Usando SNMP y RRDtools",
                     "DEF:datagramas1=segmentosRed.rrd:datagramas:AVERAGE",
                     "VDEF:datagramas1Last=datagramas1,LAST",
                     "VDEF:datagramas1First=datagramas1,FIRST",
                     "VDEF:datagramas1Max=datagramas1,MAXIMUM",
                     "VDEF:datagramas1Dev=datagramas1,STDEV",
                     "CDEF:Nivel1=datagramas1,7,GT,0,datagramas1,IF",
                     "PRINT:datagramas1Last:%6.2lf",
                     "PRINT:datagramas1First:%6.2lf",
                     "GPRINT:datagramas1Max:%6.2lf %S segEntMAX",
                     "GPRINT:datagramas1Dev:%6.2lf %S STDEV",
                     "LINE3:datagramas1#FF33D1:Datagramas enviados")

print(ret)