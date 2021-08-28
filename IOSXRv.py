from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko.tasks import netmiko_send_config, netmiko_send_command

nr = InitNornir(
    config_file="config.yaml", dry_run=True
)
S1=nr.run(netmiko_send_config, config_file="IOSXRv.txt")
S2=nr.run(netmiko_send_config, config_commands=["interface lo 8","description Norinir con VsCODE","ipv4 address 8.8.8.8 255.255.255.255","commit"])
S3=nr.run(netmiko_send_command, command_string="do show ip int brief")
S4=nr.run(netmiko_send_command, command_string="hostname equipo_4")
print_result(S1) 
print_result(S2)
print_result(S3) 
print_result(S4)