# -*- coding: utf-8 -*-
#!/usr/bin/env python
import gevent
from gevent import socket

# -*- coding: utf-8 -*-
#!/usr/bin/env python
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import scapy
from scapy.all import *
import os
import time
from threading import Thread
from superHoppingtest import *
import threading
import time
import logging



interface = "mon0"

def ch_hopp():
    while True:
        try:
            print "start"
            channel = int(random.randrange(1,13))
            #os.system("iwconfig %s channnel %d" % (interface, channel))
            try:
                proc = Popen(['iw', 'dev', interface, 'set', 'channel', channel], stdout=DN, stderr=PIPE)
                print "Obzservation Thread"
            # Next, declare a Python list to keep track of client MAC addresses
            # that we have already seen so we only print the address once per client.
                observedclients = []
            
            # The sniffmgmt() function is called each time Scapy receives a packet
            # (we'll tell Scapy to use this function below with the sniff() function).
            # The packet that was sniffed is passed as the function argument, "p".
                def sniffmgmt(p):
                # Make sure the packet has the Scapy Dot11 layer present
                    if p.haslayer(Dot11):
                    # Check to make sure this is a management frame (type=0) and that
                    # the subtype is one of our management frame subtypes indicating a
                    # a wireless client
                       # if p.type == 0 and p.subtype == 4:
            
                        # We only want to print the MAC address of the client if it
                        # hasn't already been observed. Check our list and if the
                        # client address isn't present, print the address and then add
                        # it to our list
                        print p.addr2, p.subtype, p.info
                        print "channel hop"
                        ch_hopp()
            # With the sniffmgmt() function complete, we can invoke the Scapy sniff()
            # function, pointing to the monitor mode interface, and telling Scapy to call
            # the sniffmgmt() function for each packet received. Easy!
                sniff(iface=interface, prn=sniffmgmt)                  
            except OSError:
                    sys.exit(1)
        except:
            pass
       
       
       
       
ch_hopp()       

#print "Obzservation Thread"
## Next, declare a Python list to keep track of client MAC addresses
## that we have already seen so we only print the address once per client.
#observedclients = []
#
## The sniffmgmt() function is called each time Scapy receives a packet
## (we'll tell Scapy to use this function below with the sniff() function).
## The packet that was sniffed is passed as the function argument, "p".
#def sniffmgmt(p):
#    # Make sure the packet has the Scapy Dot11 layer present
#    if p.haslayer(Dot11):
#        # Check to make sure this is a management frame (type=0) and that
#        # the subtype is one of our management frame subtypes indicating a
#        # a wireless client
#        if p.type == 0 and p.subtype == 4:
#
#            # We only want to print the MAC address of the client if it
#            # hasn't already been observed. Check our list and if the
#            # client address isn't present, print the address and then add
#            # it to our list
#            print p.addr2, p.subtype, p.info
#            print "channel hop"
#            ch_hopp()
## With the sniffmgmt() function complete, we can invoke the Scapy sniff()
## function, pointing to the monitor mode interface, and telling Scapy to call
## the sniffmgmt() function for each packet received. Easy!
#sniff(iface=interface, prn=sniffmgmt)
#
# 