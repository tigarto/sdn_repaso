## The Effects of DoS Attacks on ODL and POX SDN Controllers ##

**Enlace**: [The Effects of DoS Attacks on ODL and POX SDN Controllers](https://ieeexplore.ieee.org/document/8080058)

However, because all the packets are transmitted 
to the controller, any flooded packet from an attacker who gets access to SDN network may lead to Denial of Service (DoS) attack. 

In this paper, the effect of DoS attack on bandwidth of two communicating hosts in SDN network for Opendaylight 
(ODL) and POX controllers was investigate. We observed that the bandwidth was reduced as attack increases and the
response time was also too high. We also find out that, even after a flow table has been installed in switch, 
it was impossible for it to be reinstalled again if a 
flow timeout has been reached due to a controller handling too many packet-in events and error notification from the switches.

En este paper se analiza el impacto de un ataque DoS contra el ancho de banda entre dos host que se encuentran en una red SDN 
investigando el efecto en los controladores POX y OpenDaylight (ODL). Para el caso, al incremento del ataque produce los siguientes efectos:
* Reduccion del ancho de banda.
* Aumento en el tiempo de respuesta.
* Imposibilidad de instalar nuevas reglas para enrutar exitosamente paquetes validos.

