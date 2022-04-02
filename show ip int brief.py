from netmiko import Netmiko
from getpass2 import getpass2



password = getpass2()

cisco1 = {
    "host": "st-00891-sw5-tavm.heb.com",
    "username": "cwwuser",
    "password": getpass2(),
    "device_type": "cisco_ios",
}

net_connect = Netmiko(**cisco1)
command = "show ip int brief"

print()
print(net_connect.find_prompt())
output = net_connect.send_command(command)
net_connect.disconnect()
print(output)
print()