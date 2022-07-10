#!/usr/bin/env python3
# -*- coding: utf8 -*-

from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import logging

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)
client = ModbusClient('localhost', port=5020)
client.connect()
rq = client.write_coils(0, [True]*7, unit=1)
rq = client.write_coil(0, False, unit=1)
rq = client.write_coil(2, False, unit=1)
rq = client.write_coil(4, False, unit=1)
rq = client.write_coil(6, False, unit=1)
rq = client.write_coils(0, [False]*7, unit=1)
rq = client.write_coil(1, True, unit=1)
rq = client.write_coil(3, True, unit=1)
rq = client.write_coil(5, True, unit=1)
rq = client.write_coil(7, True, unit=1)
rq = client.write_coils(0, [False]*7, unit=1)
for y in reversed(range(8)):
    rq = client.write_coil(y, True, unit=1)
for y in reversed(range(8)):    
    rq = client.write_coil(y, False, unit=1)
for x in range(8):
    rq = client.write_coil(x, True, unit=1)
for x in range(8):    
    rq = client.write_coil(x, False, unit=1)    
client.close()  
  