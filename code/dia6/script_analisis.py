from steelscript.packets.core.pcap import PCAPReader, PCAPWriter
from steelscript.packets.core.pcap import Ethernet


print "Hola"
'''
f_read = open('./syn_attack.pcap', 'rb')

pkt_type_ethernet = 1

for pkt_ts, pkt_data, pkt_type in rdr:
    if pkt_type == pkt_type_ethernet:
        pkt = Ethernet(pkt_data)
        ip = pkt.get_layer('IP')
        if ip.pkt_name == 'IP':
            print ip.src


rdr.close()
'''