#!/usr/bin/env python3

import tkinter as tk
import tkinter.simpledialog
import os, sys, subprocess, time, re, pexpect
import signal

tk.Tk().withdraw()
#bob.geometry("+300+300")
bob=tkinter.simpledialog.askstring("VPN Connection", "Please enter the VPN password to connect to dashboards:", show='*')
print(bob)

def signal_handler(sig, frame):
        print("sighup")
        sys.exit

child = pexpect.spawn('sudo openconnect %VPNSERVER%')

child.expect('.*')
child.sendline('%USERNAME%')

child.expect('.*')
child.sendline(bob)
child.sendline('\01d')
signal.signal(signal.SIGHUP, signal_handler)


