import pyping
status = False
b1 = "broker.mqttdashboard.com"
b2 = "192.168.0.9"
porta = 1883
try:
    r = pyping.ping(b1)    # But it's udp, not real icmp
    print  (r.max_rtt,r.avg_rtt,r.min_rtt)
    status = b1,True
except Exception, e:
    localnet = pyping.ping(b2)
    print (localnet.max_rtt,localnet.avg_rtt,localnet.min_rtt)
    status = b2,True

print status