# NTEGRACION DEL REST API #

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
2. **MAC address table registration API**: Registra un par (MAC address y numero de puerto) en la tabla de direcciones MAC y agrega la entrada a la tabla de flujos del switch correspondiente.

El archivo **XXXXXXX.py** muestra como se llevo a cabo esto.

Para el caso se definen 2 clases:
1. **SimpleSwitchController**: Que es la clase que consume siendo el puente entre las peticiones GET y POST y la aplicacion asociada al Switching Hub. Esta lleva a cabo las siguientes tareas:
   * Define la URL para redicir los requerimientos HTTP.
   * Define los metodos que seran invocados al hacer peticiones HTTP a la respectiva URL.
2. **SimpleSwitchRest13**: Subclase de la aplicacion **Switching Hub** con la capacidad de actualizar la direccin MAC.
   
### Aspectos a resaltar ###

A continuación vamos a describir algunos aspectos a resaltar de las clases anteriormente mencionadas.

#### SimpleSwitchRest13 ####

A continuacion se resaltan algunos elementos de esta clase:
* **Atributos**:
  * **self.switches**: Contiene los datapaths conectados. Sigue esta forma:
  ```python
  self.switches = {
                    datapath.id1: datapath1,
                    datapath.id2: datapath2,
                    ...
                    datapath.idN: datapathN
                    
                   }
  ```
  * **self.mac_to_port**: (heredado) contiene las parejace MAC-puerto asociasos a cada datapath.
  
  ```python
  self.mac_to_port = {
                    datapath.id1: { MAC11:port11 , MAC12:port12, ..., MAC1N:port1N},
                    ...
                   }
 
  ```

* **Constructor**: en el constructor ```python __init__(...)``` se:
  * Se adquiere la instancia de la **WSGIApplication** para registrar laclase controladora.
  
  ```python
  
  class SimpleSwitchRest13(simple_switch_13.SimpleSwitch13):

    _CONTEXTS = {'wsgi': WSGIApplication} # to specify Ryu’s WSGI-compatible Web server class

    def __init__(self, *args, **kwargs):
        super(SimpleSwitchRest13, self).__init__(*args, **kwargs)
        self.switches = {}
        wsgi = kwargs['wsgi'] # Acquires the instance of WSGIApplication in order to register the controller clas
        
        # register the controller class
        wsgi.register(
                      SimpleSwitchController ''' Controller Class ''',
                      {simple_switch_instance_name: self} '''key simple_switch_api_api es empleada por el controlador para 
                                                             acceder a una instancia de la clase SimpleSwitchRest13'''
                      )

  ```
* **Metodo handler**: El metodo ```python switch_features_handler``` del padre es sobreescrito. Este evento se invoca cuando el evento SwitchFeatures es lanzado. El metodo se encarga de:
   * Adquirir el datapath a partir del evento (```python datapath = ev.msg.datapath```) y almacenarlo en ```self.switches```
   * Inicializar self.mac_to_port a vacio  (```python self.mac_to_port.setdefault(datapath.id, {})```), es decir, inicializar cada datapath sin informacion de los diferentes pares MAC:puerto .
  
```python
@set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
def switch_features_handler(self, ev):
    super(SimpleSwitchRest13, self).switch_features_handler(ev)
    datapath = ev.msg.datapath
    self.switches[datapath.id] = datapath
    self.mac_to_port.setdefault(datapath.id, {})
```

* **Metodo set_mac_to_port**: Metodo que registra la direccion MAC y el puerto en el switch especificado. Este medodo es ejecutado cuando el REST API es llamado por el metodo PUT. En el siguiente [enlace](https://osrg.github.io/ryu-book/en/html/rest_api.html) se explica y se muestra con un ejemplo el funcionamiento de este metodo.
  
#### SimpleSwitchController ####

Esta clase accepts HTTP requests to REST API. Vamos a ver los principales aspectos:
* **Adquision de la instancia SimpleSwitchRest13**: 

```python

class SimpleSwitchController(ControllerBase):

    def __init__(self, req, link, data, **config):
        super(SimpleSwitchController, self).__init__(req, link, data, **config)
        self.simple_switch_app = data[simple_switch_instance_name]

'''
Recordar previamente en el contructor de SimpleSwitchRest13:

...
def __init__(self, *args, **kwargs):
        super(SimpleSwitchRest13, self).__init__(*args, **kwargs)
        self.switches = {}
        wsgi = kwargs['wsgi']
        wsgi.register(SimpleSwitchController,
                      {simple_switch_instance_name: self})
...
'''

```

* **Implementacion del REST API's URL y su correspondiente procesamiento**: Para esto se usa el decoratorio **route** (De pronto por curiosidad puede ver el codigo [wsgi.py](https://github.com/osrg/ryu/blob/master/ryu/app/wsgi.py). En este codigo se encuentra la siguiente funcion para **route**:

```python
def route(name, path, methods=None, requirements=None):
    def _route(controller_method):
        controller_method.routing_info = {
            'name': name,
            'path': path,
            'methods': methods,
            'requirements': requirements,
        }
        return controller_method
    return _route
```

La verdad no se que es pero por el momento solo centremnos en los parametros y comparemos esto con los casos implementados en el controlador:

* **REST API para el GET**:

```python
@route('simpleswitch', url, methods=['GET'], requirements={'dpid': dpid_lib.DPID_PATTERN})
def list_mac_table(self, req, **kwargs):

    simple_switch = self.simple_switch_app
    dpid = dpid_lib.str_to_dpid(kwargs['dpid'])

    if dpid not in simple_switch.mac_to_port:
        return Response(status=404)

    mac_table = simple_switch.mac_to_port.get(dpid, {})
    body = json.dumps(mac_table)
    return Response(content_type='application/json', body=body)
```

Vemos que: 
* **name** = 'simpleswitch' (Cualquier nombre)
* **path** = '/simpleswitch/mactable/{dpid}'
* **methods** = ['GET']
* **requirements** = {'dpid': dpid_lib.DPID_PATTERN}

* **REST API para el PUT**:


```python
@route('simpleswitch', url, methods=['PUT'], requirements={'dpid': dpid_lib.DPID_PATTERN})
def put_mac_table(self, req, **kwargs):

    simple_switch = self.simple_switch_app
    dpid = dpid_lib.str_to_dpid(kwargs['dpid'])
    try:
        new_entry = req.json if req.body else {}
    except ValueError:
        raise Response(status=400)

    if dpid not in simple_switch.mac_to_port:
        return Response(status=404)

    try:
        mac_table = simple_switch.set_mac_to_port(dpid, new_entry)
        body = json.dumps(mac_table)
        return Response(content_type='application/json', body=body)
    except Exception as e:
        return Response(status=500)
```

Vemos que: 
* **name** = 'simpleswitch' (Cualquier nombre)
* **path** = '/simpleswitch/mactable/{dpid}'
* **methods** = ['PUT']
* **requirements** = {'dpid': dpid_lib.DPID_PATTERN}

La siguiente figura tomada del siguiente [enlace](https://ruslanspivak.com/lsbaws-part1/). Tengase en cuenta lo que se lleva se mostrara en formato json. 

![figura](https://ruslanspivak.com/lsbaws-part1/LSBAWS_HTTP_response_anatomy.png)

Como se mostrará en los ejemplos que se verán a continuacin se notará que se hace uso de la herramienta **curl** para hacer las peticiones **GET** y **POST** al swith. Una alternativa mas amigable y hasta empleando interfaz es por medio del uso de [postman](https://www.getpostman.com/) el cual es una herramienta para [Api Testing](https://en.wikipedia.org/wiki/API_testing). Un tutorial que muestra como usarlo se muestra en el enlace [Interactive Ryu with Postman](https://inside-openflow.com/2016/06/23/interactive-ryu-with-postman/)


### Ejemplos ###

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
 
