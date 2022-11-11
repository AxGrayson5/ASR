#!/usr/bin/env python
import rrdtool
ret = rrdtool.create("segmentosRed.rrd",
                     "--start",'N',
                     "--step",'300',
                     "DS:multicastOut:COUNTER:120:U:U",
                     "DS:paquetesIp:COUNTER:120:U:U",
                     "DS:ICMP:COUNTER:120:U:U",
                     "DS:segmentos:COUNTER:120:U:U",
                     "DS:datagramas:COUNTER:120:U:U",
                     "RRA:AVERAGE:0.5:1:300",
                     "RRA:AVERAGE:0.5:1:300",
                     "RRA:AVERAGE:0.5:1:300",
                     "RRA:AVERAGE:0.5:1:300",
                     "RRA:AVERAGE:0.5:1:300")

if ret:
    print (rrdtool.error())