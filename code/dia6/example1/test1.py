from steelscript.packets.core.pcap import PCAPReader, PCAPWriter
from steelscript.packets.core.inetpkt import Ethernet
from steelscript.packets.query.pcap_query import PcapQuery
from steelscript.wireshark.core.pcap import PcapFile

import pandas as pd

pcap_file = PcapFile('./syn_attack.pcap')
print pcap_file.info()
f_read = open('./syn_attack.pcap', 'rb')


rdr = PCAPReader(f_read)
pkt_type_ethernet = 1
paquetes = rdr.pkts()



'''
Time
 First packet: 2013-04-24 22:09:30
 Last packet : 2013-04-24 22:10:26
'''

print("Time")
print " First packet:" ,  str(pd.to_datetime(paquetes[0][0], unit='s'))
print " Last packet :" ,  str(pd.to_datetime(paquetes[len(paquetes) - 1][0], unit='s'))

'''
Statistics
 Packets      : 145
 Time span (s): 55.364
 Average pps  : 2.6
'''

num_pkt = len(paquetes)
time_span =  paquetes[len(paquetes) - 1][0] - paquetes[0][0]
avg_pps = num_pkt/time_span

print "Statistics"
print " Packets      :" ,  num_pkt
print " Time span (s):" , time_span
print " Average pps  :",  avg_pps

#print(paquetes[0]), type(paquetes[0][1].itemsize)

#print(len(paquetes[0][1]))
#pcap_q = PcapQuery(paquetes)




'''
cnt_pkt = 0
for p in paquetes:
    print pd.to_datetime(str(p[0]), unit='s')
    cnt_pkt += len(p[1])

print(cnt_pkt)


for pkt_ts, pkt_data, pkt_type in rdr:
    if pkt_type == pkt_type_ethernet:
        pkt = Ethernet(pkt_data)
        ip = pkt.get_layer('IP')
        if ip.pkt_name == 'IP':
            print ip.src

'''
rdr.close()