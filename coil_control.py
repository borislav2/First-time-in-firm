
#!/usr/bin/env python3
# -*- coding: utf8 -*-

from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import logging
import time

unit = 1

def main():
    logging.basicConfig()
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)

    client = ModbusClient(method='rtu', port='COM6', baudrate=9600, timeout=1)
    client.connect()

    first = [False, True, False, True, False, True, False, True]
    second = [True, False, True, False, True, False, True, False]

    rq = client.write_coils(0, [False]*8, unit=unit)
    assert(rq.function_code < 0x80)

    rq = client.write_coils(0, [True]*8, unit=unit)
    time.sleep(1)
    assert(rq.function_code < 0x80)


    rq = client.write_coils(0, first, unit=unit)
    time.sleep(0.5)
    rq = client.write_coils(0, [False]*8, unit=unit)
    time.sleep(1)
    assert(rq.function_code < 0x80)

    rq = client.write_coils(0, second, unit=unit)
    time.sleep(0.5)
    rq = client.write_coils(0, [False]*8, unit=unit)
    time.sleep(2)
    assert(rq.function_code < 0x80)

    for i in reversed(range(8)):
        rq = client.write_coil(i, True, unit=unit)
        time.sleep(1) #1 sec
        rq = client.write_coil(i, False, unit=unit)
        assert(rq.function_code < 0x80)     

    for j in range(8):
        rq = client.write_coil(j, True, unit=unit)
        time.sleep(1) #100 ms
        rq = client.write_coil(j, False, unit=unit) 
        assert(rq.function_code < 0x80)     
    
    client.close()  
  
if __name__ == "__main__":
    main()
