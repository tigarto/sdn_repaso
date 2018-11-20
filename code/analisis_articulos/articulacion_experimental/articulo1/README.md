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

8. **Cosas por probar**: how to change the ip address of docker container?
* https://forums.docker.com/t/ip-address-for-container/27454/6 (para ver si no tiene que ser la de docker0 -- probarlo en el ejemplo de abajo ---> docker run -d --ip="192.168.20.173" wordpressmysql).
* https://jpetazzo.github.io/2013/10/16/configure-docker-bridge-network/
* https://groups.google.com/forum/#!topic/docker-user/uR0DVb0aKi4

## Enlaces ##

* **Hping3**:
  * https://www.redeszone.net/gnu-linux/hping3-manual-de-utilizacion-de-esta-herramienta-para-manipular-paquetes-tcp-ip/
  * https://null-byte.wonderhowto.com/how-to/hack-like-pro-conduct-active-reconnaissance-your-target-with-hping3-0148092/
  * https://www.welivesecurity.com/la-es/2015/02/02/manipulando-paquetes-hping3/
  * https://www.pedrocarrasco.org/manual-practico-de-hping/
  * https://tools.kali.org/information-gathering/hping3
  * https://www.radarhack.com/tutorial/hping2.pdf
  * http://wiki.hping.org/94
  * https://asecuritysite.com/dicontent/lab02_02.pdf
  * http://knight.segfaults.net/EEE473Labs/Lab%205/Lab%205.htm
  * http://lms.uop.edu.jo/lms/pluginfile.php/403/mod_resource/content/0/Lab-Hping3.pdf
  * https://books.google.com.co/books?id=coJkCAAAQBAJ&pg=PA37&lpg=PA37&dq=hping3+lab&source=bl&ots=vwHlIoIWQa&sig=zRrcraCFsHkZMCHzEmyDfJRfYCw&hl=es&sa=X&ved=2ahUKEwj8wKeE_OPeAhXI2VMKHd2xAkk4ChDoATADegQIBRAB#v=onepage&q=hping3%20lab&f=false
  * https://f5-agility-labs-ddos.readthedocs.io/en/latest/class2/module1/lab3.html
  * https://f5-agility-labs-firewall.readthedocs.io/en/latest/class1/lab3/3a-02.html
  * http://sites.psu.edu/cvclab/wp-content/uploads/sites/24816/2016/06/ip_spoofing.pdf
  * https://pypi.org/project/llama/0.0.1a6/
  * https://github.com/deter-project/magi-modules/blob/master/hping/hping3.py
  * hping3 python github
  * https://github.com/fishman/hpingparser
  * https://github.com/kaosV20/pyDoS (ojo)
  * https://blog.sflow.com/2018/04/onos-measurement-based-control.html (con sdn)

* **tcpdump**: Podría ser usado como alternativa a wireshark.
  * https://danielmiessler.com/study/tcpdump/
  
* **iperf**:
  * https://openmaniak.com/es/iperf.php
  * https://seguridadyredes.wordpress.com/2008/06/18/iperf-midiendo-ancho-de-banda-entre-dos-hosts/
  * https://www.es.net/assets/Uploads/201007-JTIperf.pdf
  * https://www.cs.unc.edu/Research/geni/geniEdu/03-TcpTraffic.html
  * https://onl.wustl.edu/Tutorial/Filters,_Queues_and_Bandwidth/Using_Iperf_With_TCP.html
  * https://www.tlm.unavarra.es/~daniel/docencia/tar/tar14_15/practicas/practica1-iperf.pdf
  * https://resources.netbeez.net/hubfs/iPerf%20Bandwidth%20Webinar.pdf
  * http://vip.gatech.edu/wiki/images/e/ee/Lab_2_Iperf_Command.pdf
  * http://csie.nqu.edu.tw/smallko/sdn/iperf_mininet.htm (ojo)
  * https://github.com/cucl-srg/L50/wiki/About-Lab-1:-ping,-traceroute,-iperf
  * https://pypi.org/project/iperf3/
  * https://stackoverflow.com/questions/44519799/running-iperf-server-and-client-using-multithreading-in-python-causes-segmentati
  * http://www.jb.man.ac.uk/~jcullen/code/python/iperf_tests.py
  * https://github.com/cloudharmony/iperf/blob/master/save.sh
  * https://www.thegeekdiary.com/how-to-use-iperf-to-test-network-performance-in-linux/
  * https://stackoverflow.com/questions/25702196/how-to-save-iperf-result-in-an-output-file
  * http://www.crew-project.eu/book/export/html/196.html
  * https://books.google.com.co/books?id=IiqqCAAAQBAJ&pg=PA77&lpg=PA77&dq=export++data+traffic+to+sqlite&source=bl&ots=tmi_02sMHS&sig=olsO8a6oUsm027xGkdrpmgQZsx0&hl=es&sa=X&ved=2ahUKEwiUubGWg-TeAhUL4VMKHYhjBkMQ6AEwCnoECAEQAQ#v=onepage&q=export%20%20data%20traffic%20to%20sqlite&f=false
  
* **nprobe**:
  * https://prometheus.io/docs/prometheus/latest/storage/
  * https://www.outlyer.com/blog/top10-open-source-time-series-databases/#Prometheus
  * https://prometheus.io/docs/prometheus/latest/querying/api/
  * https://dzone.com/articles/monitoring-with-prometheus
  * https://www.ittsystems.com/best-sflow-collectors-and-analyzers/
  * https://www.pcwdld.com/free-open-source-netflow-analyzers
  * https://www.comparitech.com/net-admin/sflow-collectors-analyzers/
  * https://www.comparitech.com/net-admin/best-netflow-analyzers-collectors/
    
* **Miselanea**:
  * https://www.semanticscholar.org/paper/Stochastic-Switching-Using-OpenFlow-Shourmasti/80a3502a00757e52c7616e150d4203f8071a44a7
  * https://ieeexplore.ieee.org/document/7249166
