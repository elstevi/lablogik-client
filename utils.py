import os

from platform import system as uname
from uuid import getnode as get_mac
def config_file_location():
    if uname() == 'Linux':
        return '/etc/lablogik.conf' 
    elif uname() == 'FreeBSD':
        return '/usr/local/etc/lablogik.conf' 
    elif uname() == 'Windows':
        return 'C:/lablogik.conf' 
    else:
        assert "Unsupported platform"

def mac():
    return ':'.join(("%012X" % get_mac())[i:i+2] for i in range(0, 12, 2))

def shutdown():
    if uname() == 'Linux' or uname() == 'FreeBSD':
        shutdown_command = "poweroff"
    elif uname() == 'Windows':
        shutdown_command = "shutdown -s -f -t 00"
    os.system(shutdown_command) 

def reboot():
    if uname() == 'Linux' or uname() == 'FreeBSD':
        reboot_command = "reboot"
    elif uname() == 'Windows':
        reboot_command = "shutdown -r -f -t 00"
    os.system(reboot_command) 

