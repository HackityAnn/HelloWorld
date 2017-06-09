import time 
from zapv2 import ZAPv2

target = 'http://172.20.0.100:8080/HelloWorldAPI/HelloWorldAPI'

zap = ZAPv2()

print 'Starting target: %s' % target
scanid = zap.spider.scan(target)

time.sleep(2)
while (int(zap.spider.status(scanid)) < 100):
    print 'Spider progress %: ' + zap.spider.status(scanid)
    time.sleep(2)

print 'Spider completed!'

time.sleep(5)

print 'Starting scan: %s' % target
scanid = zap.ascan.scan(target)
print 'Started 1'
print zap.ascan.status(scanid)
while (int(zap.ascan.status(scanid)) < 100):
    print 'Scan progress %: ' + zap.ascan.status(scanid)
    time.sleep(5)

print 'Scan completed'

f = open('ZAP_output.txt','a')
hosts = zap.core.hosts
alerts = zap.core.alerts()
for each in hosts:
    print >> f, 'Hosts: ', zap.core.hosts
    print >> f, '\n\n'
for each in alerts:
    print >> f, 'Alerts: ', zap.core.alerts()
    print >> f, '\n\n'
f.close()