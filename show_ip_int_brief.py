import netmiko
import getpass



password=getpass.getpass()

cisco1 = {
    "host": "st-00891-sw5-tavm.heb.com",
    "username": "f785843",
    "password": password,
    "device_type": "cisco_ios",
}

net_connect =netmiko.Netmiko(**cisco1)
command = "show ip int brief"

#print()
#print(net_connect.find_prompt())
output = net_connect.send_command(command)
net_connect.disconnect()
print(output)
print()