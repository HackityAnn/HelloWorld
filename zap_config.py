#!/usr/bin/env python

import time
from pprint import pprint
from zapv2 import ZAPv2

target = 'http://172.20.0.100/HelloWorldAPI/HelloWorldAPI'
zap = ZAPv2()

print 'Accessing target %s' % target
zap.urlopen(target)
time.sleep(5)

zap.spider.scan(target)
time.sleep(2)
print 'Status %s' % zap.spider.status
while (int(zap.spider.status)<100):
    print 'Spider progress %: ' + zap.spider.status
    time.sleep(400)

print 'Spider completed'

time.sleep(5)

print 'Scanning target %s' % target
zap.ascan.scan(target)
while (int(zap.ascan.status) < 100):
    print 'Scan progress %: ' + zap.ascan.status
    time.sleep(600)

print 'Scan completed'

output = open("ZAP_Scan.txt","a")
output.write("Hosts: " + zap.core.hosts
output.write("Alerts: " + zap.core.alerts())
