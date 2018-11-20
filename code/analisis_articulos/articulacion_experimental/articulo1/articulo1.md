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

La siguiente figura (tomada del siguiente [enlace](https://www.mdpi.com/1999-5903/6/2/302/htm)) muestra el caso normal:

![fig_reactive](https://www.mdpi.com/futureinternet/futureinternet-06-00302/article_deploy/html/images/futureinternet-06-00302-g010-1024.png)

¿Pero que pasa en caso en el cual se esta lanzando un ataque DoS que involucre flooding (inundacion por la gran cantidad de paquetes enviados a la vez) y spoofing (por la falsificación de IPs) En este caso (suponiendo que la IP fuente de los paquetes es la falsificada) el efecto sera que la mayoria de los paquetes al ser comparados generaran muchos miss-table por lo que los paquetes seran enviados al controlador. En este caso, el controlador es inundado con paquetes para procesar y escribir flujos (dado el caso) en la tabla de flujos del switch, lo que hace que su rendimiento se vea afectado. Asi mismo, los switch buffers pueden tener un memory overflow debido a la sobrecarga de paquetes y flujos inutiles en la tabla de flujos, lo cual hara que, como resultado nungun flujo adicional pueda ser instalado en la tabla de flujos del switch. **This bottleneck to the controller may result in many packets being dropped hence low throughput and a longer delay in the network**


## Experimento ##

Enmarcandolo en la metodologia de [DDoS Experiment Methodology](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.134.7224&rep=rep1&type=pdf). Se tiene para un entorno emulado usando mininet:


1. Mecanismo de ataque: 
   * Flooding: Usando hping3.

2. Background traffic:
   * No se habla nada al respeco

3. Topologia de red:
   * Linear: dos sw y cuatro host/sw.

4. Mecanismo de defensa:
   * No se esta analizando.

5. Metricas:
   * Ancho de banda, jitter, loss rate, y otros parametros del link de red: Uso de iperf.
   * sniffing: Empleo de wireshark.
   





* https://www.semanticscholar.org/paper/Stochastic-Switching-Using-OpenFlow-Shourmasti/80a3502a00757e52c7616e150d4203f8071a44a7
* https://ieeexplore.ieee.org/document/7249166