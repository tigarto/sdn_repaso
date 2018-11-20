# Experimental Evaluation of the Impact of DoS attacks in SDN (Pendiente la edicion) #

**Enlace**: [Experimental evaluation of the impact of DoS attacks in SDN](https://ieeexplore.ieee.org/document/8215424)

## Resumen ##

En este paper se analiza el impacto de un ataque DoS contra el ancho de banda entre dos host que se encuentran en una red SDN 


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


1. **Mecanismo de ataque**: 
   * Flooding y spoofing: Usando hping3 (h1 -> h5)`: ```hping3  --flood --rand-source 10.0.0.5```

2. **Background traffic**:
   * No se habla nada al respecto

3. **Topologia de red**:
   * Linear: dos sw y cuatro host/sw.
   * Controladores evaluados: POX y ODL.

4. **Mecanismo de defensa**:
   * No se esta analizando.

5. **Metricas**:
   * **Ancho de banda, jitter, loss rate, y otros parametros del link de red**: Uso de iperf.
   * **sniffing**: Empleo de wireshark.
   
6. **Procedimiento de test**:
   1. Arrancar topologia.
   2. Arrancar controlador.
   3. Arrancar **iperf** para la medicion de las metricas.
   4. Lanzar el ataque DoS usando **hping3**

7. **Graficas y Conclusiones**:
   1. Ancho de banda entre TCP h100 y h200.
   2. Hay una disminución del ancho de banda en la red SDN, basicamente por la falta de memoria en los sw para agregar nuevos flujos associados a usuarios legitimos. Otra posible razon, sobre todo en el funcionamiento reactivo, es debida a la congestion en el controlador. 

## Enlaces ##
* https://onlinelibrary.wiley.com/doi/full/10.1002/sec.1759 (muy bueno)
* https://ac.els-cdn.com/S187705091502579X/1-s2.0-S187705091502579X-main.pdf?_tid=8fa3c64d-c8b6-4253-8542-a3d9ce440f6a&acdnat=1542754593_deed3a80644f6eabc72b6db1e0449654
* https://hal.inria.fr/hal-01401297/document
* https://arxiv.org/pdf/1808.01177.pdf
* https://arxiv.org/pdf/1710.08628.pdf
* https://profsandhu.com/cs5323_s17/alsmadi15.pdf
* https://etd.ohiolink.edu/!etd.send_file?accession=wright1513738941473344&disposition=inline
* https://pdfs.semanticscholar.org/b584/09021f87fc2919fa3800ea42d1a500af39b8.pdf

