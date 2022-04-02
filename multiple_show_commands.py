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
command = "show cdp neighbors"
command2 = "show vlan brief"

#print()
#print(net_connect.find_prompt())
output = net_connect.send_command(command)
output += net_connect.send_command(command2)
net_connect.disconnect()
print(output)
print()