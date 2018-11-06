# Ensayo #


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
 
