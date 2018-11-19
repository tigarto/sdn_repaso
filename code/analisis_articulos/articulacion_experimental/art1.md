# The Effects of DoS Attacks on ODL and POX SDN Controllers #

**Enlace**: [The Effects of DoS Attacks on ODL and POX SDN Controllers](https://ieeexplore.ieee.org/document/8080058)

## Resumen ##

En este paper se analiza el impacto de un ataque DoS contra el ancho de banda entre dos host que se encuentran en una red SDN 
investigando el efecto en los controladores POX y OpenDaylight (ODL). Para el caso, al incremento del ataque produce los siguientes efectos:
* Reduccion del ancho de banda.
* Aumento en el tiempo de respuesta.
* Imposibilidad de instalar nuevas reglas para enrutar exitosamente paquetes validos.

## Ataque DoS a redes SDN ##
**Finalidad**: Intentar hacer dispositivos de red como controladores, switches, computadores servidores y redes, no disponibles para usuarios validos.
**Ataque al controlador**: El objetivo de este ataque es:
1. Dificultar la labor del controlador para manejar todos lo requimientos asociados al manejo de paquetes.
2. Instalar reglas falsas en las tablas de flujo. El caso extremo se da cuando ya es imposible que nuevas reglas sean agregadas en los switches debido a que las tablas de flujo ya se llenaron (digamos que sucediob un overflow). 


**¿Que sucede cuando hay un ataque?**

La siguiente figura muestra el caso normal:

https://ai2-s2-public.s3.amazonaws.com/figures/2017-08-08/80a3502a00757e52c7616e150d4203f8071a44a7/30-Figure2-7-1.png





Normally in SDN, every packet received in port of a switch
is matched with the existing flow table. If a flow-table exists
for a packet then a packet is forwarded to outgoing port,
otherwise a packet is stored in a buffer and a packet header is
forwarded to the controller using OFPT_PACKET_IN. When a
controller is previously known to be on the outgoing port, a
flow table is installed to the switch by using
OFPT_FLOW_MOD otherwise flooding a packet to all switch
ports except an incoming port of a switch to learn the
destination.
The packet with a different source IP address means that
most of the packets will lead to packet miss in the switch flows
tables because of the packets being forwarded to the controller.
In this case, a controller will be flooded with many packets to
process and writing a flow table back to the switch. However,
the switch buffers may run out of memory because of
overloading with useless flow table. As a result, no more flow
table will be installed in the switch. This bottleneck to the
controller may result in many packets being dropped hence low
throughput and a longer delay in the network. 
