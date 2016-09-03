#!/usr/bin/env python
import pexpect
import time,sys
telconn = pexpect.spawn('telnet 192.168.100.85')
time.sleep(20)
telconn.logfile = sys.stdout
telconn.expect(":")
time.sleep(20)
telconn.send("usr" + "\r")
telconn.expect(":")
telconn.send("Pass@123" + "\r")
telconn.send("\r\n")
time.sleep(20)
telconn.expect(">")
