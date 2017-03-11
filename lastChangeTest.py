#!/usr/bin/env python
"""
Get the ifLastChange value on a loop and log it so we can figure out what
the heck NetMRI is smoking.
"""

from easysnmp import Session
import datetime

def main():
    """
    The main loop!
    """
    snmp_session = Session(hostname='10.99.1.11', community='l1ver3ad', version=2)
    interface_descrs = snmp_session.walk('.1.3.6.1.2.1.2.2.1.2')
    interface_changed = snmp_session.walk('.1.3.6.1.2.1.2.2.1.9')

    for iface in interface_descrs:
        interface_index = int(iface.oid.rsplit('.', 1)[1])
        try:
	    date_changed = datetime.datetime.now() - datetime.timedelta(seconds=int(interface_changed[interface_index].value))
            print "%i %s %s %s" %(interface_index, iface.value, interface_changed[interface_index].value, date_changed)
        except IndexError:
            break

if __name__ == "__main__":
    main()
