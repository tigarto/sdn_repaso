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
      3. **Capa de aplicación**: Son los programas que se ejecutan en el controlador

* http://tech4b.blogspot.com/2012/04/how-software-defined-networking-will.html
* https://qmonnet.github.io/whirl-offload/2016/07/08/introduction-to-sdn/

