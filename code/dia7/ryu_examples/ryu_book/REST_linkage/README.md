# Ensayo #

INTEGRACION DEL REST API

## Conceptos de utilidad ##

Puede que sea necesario en algun momento darles una ojeada, por lo tanto se ponen como fuente de consulta a futuro:
1. [Python - Network Programming](https://www.tutorialspoint.com/python/python_network_programming.htm)
Conocimientos que podrian ser de utilidad:
2. WSGI: 
   * [wsgi.readthedocs.io](https://wsgi.readthedocs.io/en/latest/)
   * [Basics of WSGI](https://www.agiliq.com/blog/2013/07/basics-wsgi/)
   * [Let’s Build A Web Server. Part 1.](https://ruslanspivak.com/lsbaws-part1/)
   * [Let’s Build A Web Server. Part 2.](https://ruslanspivak.com/lsbaws-part2/)
   * [Let’s Build A Web Server. Part 3.](https://ruslanspivak.com/lsbaws-part3/)

## Objetivo ##

En general, lo que se busca mostrar es como permitir que una aplicación en Ryu pueda interactuar con otros sistemas o browser, que se hace, al agregar funciones REST link en la aplicacion. En el caso, lo que se busca se explica por medio de la siguiente figura (tomada del siguiente [enlace](https://blog.appdynamics.com/engineering/an-introduction-to-python-wsgi-servers-part-1/)):

![WSGI Interface](https://46zwyrvli634e39iq2l9mv8g-wpengine.netdna-ssl.com/wp-content/uploads/2016/05/g5dlafgwtz05_cpptiktuiqbj6isrtjtxvejauutz58vkwtl1je7y2n9bnu1tmf_ofggmhd0xegrn2dlee6en4tpq9x-8kmlgmhgfucb7erjetcdzg9qrbldwgm7gmdyekj5dri5.png)

Al crear un REST API, es posible que la aplicación Ryu (en este caso el **Switching Hub**) pueda interactuar con peticiones hechas desde un navegador. Para el caso dichas peticiones se harán por medio de peticiones GET y PUT empleando la aplicacion curl.

## Sobre el ejemplo ##

Este ejemplo fue tomado de [REST Linkage](https://osrg.github.io/ryu-book/en/html/rest_api.html). El objetivo es agregar una REST link function al **Switching Hub**.

### Implementando las funciones del REST Api ###

Es importante definir lo que hará cada una de las funciones del REST Api. Para el caso se implementarán las siguientes:
1. **MAC address table adquisition API**: Retorna el contenido de la tabla MAC asociada al switch. Lo que devuelve es un para formato JSON de la direccion MAC y el numero de puerto correspondiente.
2 **MAC address table registration API**: Registra un par (MAC address y numero de puerto) en la tabla de direcciones MAC y agrega la entrada a la tabla de flujos del switch correspondiente.

El archivo []()

### Comandos ###

### Test 1 ###

1. Arrancando la topologia
```
sudo mn --topo single,3 --mac --switch ovsk --controller remote 
```

2. Configurando el switch

```
sudo ovs-vsctl set Bridge s1 protocols=OpenFlow13
```

3. Arrancando el controlador

```
ryu-manager --verbose simple_switch_rest_13.py
```

4. Haciendo ping entre h1 y h2

```
h1 ping -c 1 h2
```

5. Peticion get al controlador

```
curl -X GET http://127.0.0.1:8080/simpleswitch/mactable/0000000000000001
```

6. Detenga el controlador y mininet.

### Test 1 ###

1. Arrancando la topologia
```
sudo mn --topo single,3 --mac --switch ovsk --controller remote 
```

2. Configurando el switch

```
sudo ovs-vsctl set Bridge s1 protocols=OpenFlow13
```

3. Arrancando el controlador

```
ryu-manager --verbose simple_switch_rest_13.py
```

4. Peticion put al controlador

```
curl -X PUT -d '{"mac" : "00:00:00:00:00:01", "port" : 1}' http://127.0.0.1:8080/simpleswitch/mactable/0000000000000001

curl -X PUT -d '{"mac" : "00:00:00:00:00:02", "port" : 2}' http://127.0.0.1:8080/simpleswitch/mactable/0000000000000001
```

5. Hacer ping entre los h1 y h2. Para el caso se notara una menor demora.

```
h1 ping -c 1 h2
```

<!---
-Las operaciones más importantes que nos permitirán manipular los recursos son cuatro: GET para consultar y leer, POST para crear, PUT para editar y DELETE para eliminar.

Para terminar, comentar que lo más importante a tener en cuenta al crear nuestro servicio o API REST no es el lenguaje en el que se implemente sino que las respuestas a las peticiones se hagan en XML o JSON, ya que es el lenguaje de intercambio de información más usado.

Algunos frameworks con los que podremos implementar nuestras APIs: Las más usadas son JAX-RS y Spring Boot para Java, Django REST framework para Python, Laravel para PHP o Restify para Node. js


https://www.codecademy.com/articles/what-is-rest
https://www.restapitutorial.com/

-----------------------------------
https://en.wikipedia.org/wiki/Web_framework



http://www.python.org.ar/wiki/WSGI
http://wsgi.tutorial.codepoint.net/
https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface


https://ruslanspivak.com/lsbaws-part1/

https://webob.org/
https://docs.pylonsproject.org/projects/webob/en/stable/

https://romain.dorgueil.net/blog/en/python/2011/08/22/wsgi-the-first-steps.html
https://www.oreilly.com/library/view/python-web-frameworks/9781492037873/ch04.html

--->
 
