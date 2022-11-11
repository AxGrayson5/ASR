import time
import rrdtool
from getSNMP import consultaSNMP
while 1:
    #tcp_in_segments = int(
        #consultaSNMP('comunidadSNMP','localhost',
                     #'1.3.6.1.2.1.6.10.0'))
    #tcp_out_segments = int(
        #consultaSNMP('comunidadSNMP','localhost',
                     #'1.3.6.1.2.1.6.11.0'))
    multicast_out = int(
        consultaSNMP('comunidadASR', 'localhost',
                     '1.3.6.1.2.1.2.2.1.18.2'))
    paquetesIP_out = int(
        consultaSNMP('comunidadASR', 'localhost',
                     '1.3.6.1.2.1.4.10.0'))
    ICMP_in = int(
        consultaSNMP('comunidadASR', 'localhost',
                     '1.3.6.1.2.1.5.1.0'))
    segmentos_re = int(
        consultaSNMP('comunidadASR', 'localhost',
                     '1.3.6.1.2.1.6.12.0'))
    datagramas_out = int(
        consultaSNMP('comunidadASR', 'localhost',
                     '1.3.6.1.2.1.7.4.0'))
    valor = "N:" + str(multicast_out) + ':' + str(paquetesIP_out) + ":" + str(ICMP_in) + \
            ":" + str(segmentos_re) + ":" + str(datagramas_out)
    print (valor)
    rrdtool.update('segmentosRed.rrd', valor)
   # rrdtool.dump('traficoRED.rrd','traficoRED.xml')
    time.sleep(1)

if ret:
    print (rrdtool.error())
    time.sleep(300)