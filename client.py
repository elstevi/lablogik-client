import ConfigParser
import requests
import os
import utils

from polling_loop import enter_polling_loop
from time import sleep

# Import configuration
config = ConfigParser.ConfigParser()
config.readfp(open(utils.config_file_location()))

hosts   = config.get('lablogik-client', 'hosts')
scheme  = config.get('lablogik-client', 'scheme')
timeout = int(config.get('lablogik-client', 'timeout'))
url     = config.get('lablogik-client', 'url')

# For each host in the configuration, fork a process
for host in hosts.split(','):
    newpid = os.fork()
    if newpid == 0:
        fullurl = "%s://%s%s?mac=%s" % (scheme, host, url, utils.mac())
        enter_polling_loop(fullurl, timeout)
