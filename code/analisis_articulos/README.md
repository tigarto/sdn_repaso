# Analisis de articulos #

> Este analisis se hace como punto de partida para el reporte a escribir sobre **Ataques de denegación de servicio en redes definidas por software**

## Ataques de denegación de servicio en redes definidas por sofware ##

### Conceptos preliminares ###

> A continuación se muestran definiciones preliminares con el fin de facilitar la comprención de contenidos relativos al tema que seran tratados mas adelante.

1. **Arquitectura SDN**: Arquitectura donde se separa la capa de control de la de datos. Tal y como se muestra en la siguiente figura (Tomada de: https://qmonnet.github.io/whirl-offload/2016/07/08/introduction-to-sdn/)

![sdn_arch](https://qmonnet.github.io/whirl-offload/img/misc/sdn.svg)

2. **Componentes de la arquitectura**: Basicamente se hablan de capas e interfaces. 
   1. **Capas**:
      1. **Capa de control**: Software que se ejecuta en un servidor. Esta encargada de controlar la red y es analogo a un Sistema operativo pues abstrae la red a las aplicaciones para que estas puedan interactuar con esta sin conocer detalles de bajo nivel.
      2. **Capa de datos**: Capa compuesta por los switches Openflow (tambien llamados forwarding elements). Esta se encarga de encaminar (enrutar, dirigir) los paquetes a traves de la red.
      3. **Capa de aplicación**: Son los programas que se ejecutan en el controlador. Son escritos por el programador usando APIs para definir la logica de la red. Las aplicaciones pueden implementar algoritmos y protocolos para controlar la red. Tambien pueden hace cosas como reconfigurar rapidamente la red en caso de ser necesario.
      
   2. **Interfaces**:
      1.  **Interfaz norte (north bound interface)**: Interfaz que comunica las aplicaciones con el controlador. Esta interfaz es ofrecida por el controlador para permitir que aplicaciones se puedan ejecutar sobre este. Este API del controlador esta destinado a proporsionar la abstraccion de los dispositivos de red y la topologia. 
      2.  **Interfaz sur (south bound interface)**: Interface que comunica la capa de controlador (controlador) con la capa de datos. La interfaz mas comun es el protocolo **Openflow**.

La siguiente figura tomada del siguiente [enlace](https://www.opennetworking.org/sdn-definition/) muestra esto:

![capas](https://3vf60mmveq1g8vzn48q2o71a-wpengine.netdna-ssl.com/wp-content/uploads/2017/06/sdn-architecture-img.jpg)

3. **Tablas de flujos (flow tables)**: Es la estructura de datos fundamental de un dispositivo SDN. Estas permiten a un dispositibo evaluar los paquetes de ingreso (incoming packets) y tomar la accion apropiada basada en los contenidos del paquete recien recibido, en resumen, en estas estructuras se implementan las politicas. Una tabla de flujos consiste de un numero de entradas de flujo priorizadas (prioritized flow entries) o reglas.

4. **Reglas**: Cada una de las entradas de la tabla de flujos, cada una consistente basicamente de dos componentes **match fields** y **actions**. Estas definen la manera como seran direccionados (tratados) los paquetes que ingresan al switch. (como lo muestra la imagen tomada del siguiente [enlace](
https://www.slideshare.net/AzharHKhuwajaMEngMEF/sdn-fundamentals-short-presentation)).

![flow rule](https://image.slidesharecdn.com/sdnfundamentals-shortpresentation-161122162211/95/sdn-fundamentals-short-presentation-28-638.jpg?cb=1479831766)

Gracias a que la parte asociada al **match** tiene campos asociados a elementos de la capas L2, L3 y L4, un switch puede funcionar como diferentes dispositivos de red segun las reglas agregadas (Tal y como se muestra en la siguiente figura tomada del siguiente [enlace](https://www.slideshare.net/joelwking/introduction-to-openflow-41257742)).

![funciones](https://image.slidesharecdn.com/introductiontoopenflow-141107081421-conversion-gate02/95/introduction-to-openflow-19-638.jpg?cb=1415710317)

5. **Flujo (flow)**: Es una secuencia de paquetes que va desde una fuente a un destino ([definicion de wikipedia](https://en.wikipedia.org/wiki/Traffic_flow_(computer_networking))). En el siguiente [enlace](https://www.quora.com/What-is-network-flow) se muestra una buena analogia.

6. **Mensajes Openflow**: En el siguiente [enlace](http://wwwaem.brocade.com/content/html/en/deployment-guide/brcd-fastiron-openflow-dp/GUID-95D41B2F-E3D4-45FE-8992-52674D73DA4F.html) se muestra una lista de mansajes Openflow. Otro enlace que puede ser bueno revisar es el [siguiente](https://overlaid.net/2017/02/15/openflow-basic-concepts-and-theory/). La siguiente figura tomada de las diapositivas [Introductionn to Openflow](https://www.slideshare.net/joelwking/introduction-to-openflow-41257742) muestran estos mensajes graficamente:

![mensajes](
https://image.slidesharecdn.com/introductiontoopenflow-141107081421-conversion-gate02/95/introduction-to-openflow-36-638.jpg?cb=1415710317)

    A continuacion se hablan de algunos mensajes de importancia de los anteriormente mostrados:
   * **Packer_In message**: Mensaje enviado desde el switch al controlador. Este indica un **Table_miss event**.
   * **Packet_Out message**: Mensaje enviado desde el controlador al switch para cosas para que el switch haga una actividad de forwarding (reenvio) de este.

7. **Matching**: Comparación entre un paquete y las reglas almacenada en la tabla de flujos de un switch. Cuando la regla es encontrada se aplican las acciones dictadas por esta sobre el paquete. Cuando pasa lo contrario, se produce un **Table_miss event** indicando que no se encontro una regla asociada al paquete. La siguiente figura (obtenida del siguiente [enlace](https://etherealmind.com/sdn-use-case-firewall-migration-in-the-enterprise/)) ilustra esto: 

![matching](https://etherealmind.com/wp-content/uploads/2013/03/sdn-firewall-migration-6.png)

El proceso de matchin se rigue por la siguiente grafica (obtenida de: [Software-Defined Networking Using OpenFlow: Protocols, Applications and Architectural Design Choices](https://www.mdpi.com/1999-5903/6/2/302/htm)):

![algo_matching](https://www.mdpi.com/futureinternet/futureinternet-06-00302/article_deploy/html/images/futureinternet-06-00302-g003-1024.png)


8. **Insersion proactiva u reactiva**: 
   * https://www.slideshare.net/joelwking/introduction-to-openflow-41257742 
   * http://networkstatic.net/openflow-proactive-vs-reactive-flows/
   
9. **Aplicaciones internas y externas**

10. **Ataques de denegacion de servicio**: Un ataque de denegacion de servicio es un ataque a una red con el fin de hacer el servicio inaccesibla para usuarios legitimos. Normalmente proboca la perdida de conectividad por el alto consumo de ancho de banda de la red victima o la sobrecarga de los sistemas que la conforman. En [A Cisco Guide to Defending Against Distributed Denial of Service Attacks](https://www.cisco.com/c/en/us/about/security-center/guide-ddos-defense.html) se hace una buena descripción sobre estos. 

11. **IP Spoofing**: Ataque que sucede cuando un atacante envia paquetes con una dirección IP fuente falsa con el fin de consumir los recursos de la victima. Existen otros tipos de ataques tipo spoofing como ARP Spoofing y DNS Spoofing por citar algunos (ver: https://www.springboard.com/blog/spoofing-attacks/). Este enlace hace una ilustracion muy buena: https://blog.cloudflare.com/the-root-cause-of-large-ddos-ip-spoofing/. La siguiente figura tomada de [Spoofing Attacks: Understanding What They Are and How to Prevent Them](https://www.springboard.com/blog/spoofing-attacks/)

![IP_spoofing](https://www.springboard.com/blog/wp-content/uploads/2018/06/image1.jpg)


## Enlaces a la loca ##
* https://idea.popcount.org/2016-09-20-strange-loop---ip-spoofing/
* https://www.networkworld.com/article/2268110/lan-wan/chapter-1--understanding-network-security-principles.html?page=4
* https://www.springboard.com/blog/spoofing-attacks/
* https://blog.cloudflare.com/the-root-cause-of-large-ddos-ip-spoofing/
* https://www.springboard.com/blog/spoofing-attacks/
* https://www.cisco.com/c/en/us/about/press/internet-protocol-journal/back-issues/table-contents-38/104-ip-spoofing.html
* https://blog.cloudflare.com/the-root-cause-of-large-ddos-ip-spoofing/
* https://www.sans.org/reading-room/whitepapers/threats/spoofed-ip-address-distributed-denial-service-attacks-defense-in-depth-469
* http://tech4b.blogspot.com/2012/04/how-software-defined-networking-will.html
* https://qmonnet.github.io/whirl-offload/2016/07/08/introduction-to-sdn/
* https://www.slideshare.net/AzharHKhuwajaMEngMEF/sdn-fundamentals-short-presentation
* https://www.osapublishing.org/oe/fulltext.cfm?uri=oe-19-26-B421&id=224728
* https://overlaid.net/2017/02/15/openflow-basic-concepts-and-theory/
* https://www.slideshare.net/joelwking/introduction-to-openflow-41257742
* https://www.slideshare.net/bbsali0/the-potential-impact-of-software-defined-networking-sdn-on-security/45-Where_to_Begin
* http://mbat-cctu.nsysu.edu.tw/data/SDN_NFV_class/ (enlace como bueno)
* http://www.linux-magazine.com/Issues/2014/162/OpenFlow
* https://etherealmind.com/sdn-use-case-firewall-migration-in-the-enterprise/
* https://www.mdpi.com/1999-5903/6/2/302/htm


