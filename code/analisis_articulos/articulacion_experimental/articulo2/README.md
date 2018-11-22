# Experimental Evaluation of the Impact of DoS attacks in SDN (Pendiente la edicion) #

**Enlace**: [Experimental evaluation of the impact of DoS attacks in SDN](https://ieeexplore.ieee.org/document/8215424)

## Resumen ##

En este parer se investiva un rango de ataques DoS contra redes SDN basadas en OpenFlow (OpenFlow based SDN), ambos contra el plano de control y contra el plano de datos. Se cuantifica ademas el impacto de los ataques via experimentos. Experimentalmente se compara el impacto usando tres controladores distintos: ONOS, Ryu y Floodlight. Los resultados muestran que con recursos relativamente limitados, un atacante puede causar una significativa interrupción contra una SDN.

## Sobre los ataques ##
1. **Objetivo del ataque**: Consumir los recursos de la victima.
2. Se consideran (en este paper) dos tipos de ataques:
   1. Ataques contra el plano de control (controlador): 
      * En este lo que se busca es inabilitar al controladoir para manejar nuevos flujos e instalr nuevas reglas reactivamente.
   2. Ataques contra el plano de datos (swtiches): Aqui el atacante puede tener como objetivos:
      1. Agotamiento (consumo -- exhaustion) de la memoria para almacenar la reglas de forwarding.
      2. Consumo de los recursos de computo requeridos para realizar el envio de paquetes (paque fowwarding).

## Coceptos basicos necesarios recordas (por si se le han olvidado) ##
1. Las 3 capas (dato, control y aplicacion).
2. Las 2 intrerfaces (sur y norte).
3. forwarding rulas: se instalan via flow_mode messages.
4. match-action paradigm.
5. Instalacion de las reglas: Proactiva y reactiva.
6. Table_Miss event.
7. Packet-In message.
8. Packet-Out message.
9 Los Table_Miss event y sus correspondientes mensajes Openflow son operaciones respectivamente costosas para un controlador, y por ende, esto puede ser explotado por un atacante.

## Experimentos ##

### Experimento 1 - Ataque al plano de control ###

Enmarcandolo en la metodologia de [DDoS Experiment Methodology](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.134.7224&rep=rep1&type=pdf). Se tiene para un entorno emulado usando mininet:

1. **Mecanismo de ataque**: 
   * [Packet crafting](https://en.wikipedia.org/wiki/Packet_crafting): 
     * Envio de paquetes IP (TCP o UDP) con direcciones IP fuente y destino asi como MAC aleatoriamente generadas. Para lo cual se usa scapy a una tasa maxima de 500 pkts/s --> se genera un pcap.
     * Uso de tcpreplay: usado para reproducir el archivo pcap preamente generado hasta una tasa de 70000 pkts/s.

2. **Background traffic**:
   * No se habla nada al respecto

3. **Topologia de red**:
   * Single: un sw (s1) y tres host (h1, h2, h3).
     * h1: El atacante.
     
   * Controladores evaluados: Ryu, ONOS, Floodlight. El controlador corre la aplicacion asociada a los switch.

4. **Mecanismo de defensa**:
   * No se esta analizando.

5. **Metricas**:
   * **Packet delivery ratio**
   * **Controllerv CPU load**: 
   
7. **Graficas y Conclusiones**:
   1. **Descripción sobre lo que pasa en el ataque**:
      1. Los paquetes lanzados desde h1 llegan s s1 ppor el puerto p1.
      2. Direcciones aleatorias --> No hay matching rule instalada --> se envia uel paquete al controlador.
      3. El controlador envia de nuevo el paquete al s1 usando packet_Out mess con la accion Flooding. 
      4. Se envian todos los paquetes por los puertos p1 y p2 alcanzando a h2 y h3, sin embargo no hay respuesta de estos pues ninguno es el destino. 
   2. Si se incrementa la tasa de envio, el atacante puede consumir una cantidad considerable de los recuros del controlador hasta el punto de hacerlo incapaz de manejar flujos legitimos.
   
### Experimento 2 - Ataque al plano de datos ###
El objetivo para este caso es consumir las TCAM memory en switches cuando estos son de hardware recursos de computo cuando estos son de software. Lo anterior impacta la capacidad para la transferencia (forwarding) de paquetese legitimos.  

Lo que se evalua en el experimento es la capacidad del switch para transferencia de paquetes independientemente del controlador, por lo que se asume que las reglas de transferencia relevantes para el manejo del trafico son preinstaladas en el switch.

* **¿Que sucede en este ataque?**
  1
1. **Mecanismo de ataque**: 
   * [Packet crafting](https://en.wikipedia.org/wiki/Packet_crafting): 
     * Envio de paquetes IP (TCP o UDP) con direcciones IP fuente y destino asi como MAC aleatoriamente generadas. Para lo cual se usa scapy a una tasa maxima de 500 pkts/s --> se genera un pcap.
     * Uso de tcpreplay: usado para reproducir el archivo pcap preamente generado hasta una tasa de 70000 pkts/s.

2. **Background traffic**:
   * No se habla nada al respecto

3. **Topologia de red**:
   * Single: un sw (s1) y tres host (h1, h2, h3).
     * h1: El atacante.
     
   * Controladores evaluados: Ryu, ONOS, Floodlight. El controlador corre la aplicacion asociada a los switch.

4. **Mecanismo de defensa**:
   * No se esta analizando.

5. **Metricas**:
   * **Packet delivery ratio**
   * **Controllerv CPU load**: 
   
7. **Graficas y Conclusiones**:
   1. **Descripción sobre lo que pasa en el ataque**:
      1. Los paquetes lanzados desde h1 llegan s s1 ppor el puerto p1.
      2. Direcciones aleatorias --> No hay matching rule instalada --> se envia uel paquete al controlador.
      3. El controlador envia de nuevo el paquete al s1 usando packet_Out mess con la accion Flooding. 
      4. Se envian todos los paquetes por los puertos p1 y p2 alcanzando a h2 y h3, sin embargo no hay respuesta de estos pues ninguno es el destino. 
   2. Si se incrementa la tasa de envio, el atacante puede consumir una cantidad considerable de los recuros del controlador hasta el punto de hacerlo incapaz de manejar flujos legitimos.


   
## Enlaces ##
* https://onlinelibrary.wiley.com/doi/full/10.1002/sec.1759 (muy bueno)
* https://ac.els-cdn.com/S187705091502579X/1-s2.0-S187705091502579X-main.pdf?_tid=8fa3c64d-c8b6-4253-8542-a3d9ce440f6a&acdnat=1542754593_deed3a80644f6eabc72b6db1e0449654
* https://hal.inria.fr/hal-01401297/document
* https://arxiv.org/pdf/1808.01177.pdf
* https://arxiv.org/pdf/1710.08628.pdf
* https://profsandhu.com/cs5323_s17/alsmadi15.pdf
* https://etd.ohiolink.edu/!etd.send_file?accession=wright1513738941473344&disposition=inline
* https://pdfs.semanticscholar.org/b584/09021f87fc2919fa3800ea42d1a500af39b8.pdf

