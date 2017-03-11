#!/usr/bin/env python
"""
Get the ifLastChange value on a loop and log it so we can figure out what
the heck NetMRI is smoking.
"""

from easysnmp import Session

def main():
    """
    The main loop!
    """
    snmp_session = Session(hostname='10.99.1.11', community='l1ver3ad', version=2)
    interface_descrs = snmp_session.walk('.1.3.6.1.2.1.2.2.1.2')
    interface_changed = snmp_session.walk('.1.3.6.1.2.1.2.2.1.9')
    print interface_descrs

if __name__ == "__main__":
    main()
