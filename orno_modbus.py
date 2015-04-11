#!/usr/bin/python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.pdu import ModbusRequest
import sys


# Sends password to ORNO meter to open a 10-second write window.
class SendOrnoPassword(ModbusRequest):
  function_code = 0x28
  _rtu_frame_size = 13

  def __init__(self, password, **kwargs):
    ModbusRequest.__init__(self, **kwargs)
    self.password = password

  def encode(self):
    prefix = '\xfe\x01\x00\x02'
    passwordBytes = [int(self.password[i:i+2], 16) for i in range(0, len(self.password), 2)]
    return prefix + chr(len(passwordBytes)) + "".join(map(chr, passwordBytes))


# Changes the address of an ORNO OR-WE-504 meter.
def main():
  if len(sys.argv) != 4:
    print(
"""Usage: ./orno_modbus.py serial_port device_address target_device_address
Example: ./orno_modbus.py /dev/ttyUSB0 1 11

If you have only one device you can set the device_address to 0 to change its address.
""")
    sys.exit(0)

  port = sys.argv[1]
  address = int(sys.argv[2])
  target_address = int(sys.argv[3])

  client = ModbusClient(method="rtu", port=port, baudrate=9600)
  client.connect()

  request = SendOrnoPassword('00000000', unit=address)
  client.execute(request)

  response = client.write_registers(15, [target_address], unit=address)
  if response:
    if address:
      print "Success. Changed address from %d to %d." % (address, target_address)
    else:
      print "Success. Changed address to %d." % (target_address)
  else:
    print "Address change failed"

  client.close()


if __name__ == "__main__":
  main()
