Python library for interacting with the Orno OR-WE-504 power meter.

```
Usage: ./orno_modbus.py serial_port address target_address

Example: ./orno_modbus.py /dev/ttyUSB0 1 12
  Changes the address of a device at address 1, setting its address to 12.
```

## Po polsku

Licznik energii ORNO OR-WE-504 jest bardzo fajnym urządzeniem, z którego można odczytywać stan licznika i inne parametry
(np. moc chwilową) przy pomocy protokołu MODBUS przez łącze RS-485. Aby móc podłączyć więcej niż jeden taki licznik
do magistrali MODBUS, należy pozmieniać adresy liczników tak, aby każdy był inny.
Niestety program dostarczany przez ORNO, który pozwala na zmianę adresu, działa tylko w systemie Windows XP.

Niniejszy program bazuje na bibliotece pymodbus, a funkcja wysyłania hasła do licznika jest napisana na podstawie
[kodu programu pORNO](https://git.kolosowscy.pl/jurek/pORNO) Jerzego Kołosowskiego.
