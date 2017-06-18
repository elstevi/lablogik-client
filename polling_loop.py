import requests
import utils
from time import sleep
def enter_polling_loop(url, timeout):
    while True:
        try:
            r = requests.get(url)
            if r.text.rstrip() == "hard_shutdown":
                utils.shutdown()
            elif r.text.rstrip() == "no_change":
                print "no change"
            else:
                print "Unhandled %s" % r.text
        except requests.exceptions.ConnectionError:
            print "connection failed to %s" % url 
        sleep(timeout)
