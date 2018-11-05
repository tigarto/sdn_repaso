# Switching Hub

## Aplicación a implementar ##

Implementar una aplicación en Ryu que permite programar un datapath (switch openflow) para que función como switch de capa 2.
Lo cual se realiza mediante las siguientes funciones simples:
1. Aprender la dirección MAC del hor conectado a un puerto y retenerla en la tabla de direcciones MAC.
2. Cuando se reciban paquetes dirijidos a un host que ya se ha aprendido, transferirlos al puerto al que dicho host esta conectado.
3. Cuando se reciban paquetes dirijidos a un host descnonocido, realizar flooding.

##  Implementacion ##

En el enlace [Switchng Hub](https://osrg.github.io/ryu-book/en/html/switching_hub.html) se encuentra explicado el codigo que implementa el
switch ([example_switch_13.py](./example_switch_13.py)). Para la implementacíón de dicha aplicación se sigue el Ryu application programming model
descrito en el siguiente [enlace](https://ryu.readthedocs.io/en/latest/ryu_app_api.html#ryu-application-programming-model), el cual se representa
graficamente en la siguiente figura:

![Modelo de programación de aplicaciones Ryu](https://osrg.github.io/ryu-book/en/html/_images/fig1.png)

En el siguiente [enlace](https://github.com/knetsolutions/learn-sdn-with-ryu/blob/master/ryu_part2.md) se describen, de manera resumida, los pasos para 
la implementación de una aplicación en Ryu. Estos son:
1. Importar las clases y librerias base.
2. Definir la clase asociada a la aplicación, esta será una subclase de la clase **app_manager** (```python app_manager.RyuApp```).
3. Manejar los eventos Openflow relevantes (cuando un mensaje openflow packet in es recibido), implementando handlers que atiendan los eventos que su aplicación necesita atender; esto
depende de la logica de esta.
4. Ejecutar la aplicación.

## Importancia de conocer el protocolo (o por lo menos algunos aspectos) ##

Recuerde que gracias a la abstracción sobre la red que ofrece OpenFlow no nos tenemos que ocupar por los detalles de
bajo nivel para la implementación de una aplicación que se ejecuta en el controlador para interactuar con la red. En el paso 1 anteriormente descrito se menciona la necesidad de importar clases y librerias base. Pero una cosa es importar y otra cosa es usar por dicha razon es necesario conocer no solo el modelo de programacin del controlador (anteriormente mencionado) si no con que esta este relacionado. Para el caso, este modelo esta relacionado con el protocolo Openflow, por lo tanto, el conocimiento, por lo menos de los aspectos basicos, para conocer que elemento del protocolo esta abstrayendo una clase determinada y asi poder hacer uso de objetos asociados a esta para la implementación de su lógica. Esto lo podemos reducir a dos pasos:
1. Conocimiento de la especificacin Openflow a emplear ([Enlaces con diferentes especificaciones](https://www.opennetworking.org/software-defined-standards/specifications/))
2. Conocimiento del API del controlador, el cual abstrae dicha especificación ([API de Ryu](https://ryu.readthedocs.io/en/latest/index.html))

### Algunos mensajes del protocolo empleados ###
En la pagina de [flowgramable](http://flowgrammable.org/sdn/openflow/message-layer/) se encuentran de manera resumida los diferentes mensajes Openflow. A continuación se muestran los mas importantes y la parte del API relacionada con estos. Desde el punto de vista mas basico Openflow (v1.3 para el caso) se divide en 3 componentes principales tal y como se muestra en la siguiente figura:

![OpenFlow v1.3.0 architecture](http://docs.ruckuswireless.com/fastiron/08.0.61/fastiron-08061-sdnguide/GUID-913C049F-EC28-4C54-B736-6A59100DC932-output_low.png)

Esta arquitectura muestra 3 componentes principales: el controlador, relacionado con la capa de control; el switch, relacionado con la capa de datos y el protocolo Openflow que permite la comunicacion entre los dos anteriores. Un switch Openflow posee varias tablas de flujo en las cuales se definen el comportamiento del trafico en la red, siendo el controlador el dispositivo encargado de definir el contenido de cada uno de los flujos de acuerdo a las necesidades del programador.

Cada flujo se divide basicamente en 3 campos: Matching Fields, Action List y Stats. La siguiente figura muestra la forma de una entrada tipica de la tabla de flujos para el protocolo openflow v1.3:

![OpenFlow 1.3.0 flow table entries](http://docs.ruckuswireless.com/fastiron/08.0.61/fastiron-08061-sdnguide/GUID-4B59E1AC-6945-4297-A4F5-4E2D45EB85EA-output_low.png)

Ahora procedamos a ver un poco mas los mensajes empleados y un fragmento de codigo OpenFlow relacionado con el API del controlador.

#### Packet-In Message ####

Este mensaje es la manera que tiene el switch de enviar un paquete capturado al controlador. Hay dos razones por las cuales esto paso; por la existencia de una accion explicita como el resultado de un matching para este comportamiento, o desde un miss en la parte del match de las tablas, o un error de ttl. En la siguiente figura se muestra que es el switch quien lo inicia:

![PacketIn](http://flowgrammable.org/static/media/uploads/msgs/packet_in_sequence.png)

La estructura de este mensaje para la version 1.3.0 del protocolo Openflow se muestra a continuación:

![PacketIn](http://flowgrammable.org/static/media/uploads/msgs/packet_in_1_3.png)

La parte del API de Ryu relacionada con este mensaje se encuentra en el siguiente [enlace](https://ryu.readthedocs.io/en/latest/ofproto_v1_0_ref.html#packet-in-message). 

**Clase **

```python 
class ryu.ofproto.ofproto_v1_3_parser.OFPPacketIn(datapath, buffer_id=None, total_len=None, reason=None, table_id=None, cookie=None, match=None, data=None)
```

**Ejemplo**

```python 
@set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
def packet_in_handler(self, ev):
    msg = ev.msg
    dp = msg.datapath
    ofp = dp.ofproto

    if msg.reason == ofp.OFPR_NO_MATCH:
        reason = 'NO MATCH'
    elif msg.reason == ofp.OFPR_ACTION:
        reason = 'ACTION'
    elif msg.reason == ofp.OFPR_INVALID_TTL:
        reason = 'INVALID TTL'
    else:
        reason = 'unknown'

    self.logger.debug('OFPPacketIn received: '
                      'buffer_id=%x total_len=%d reason=%s '
                      'table_id=%d cookie=%d match=%s data=%s',
                      msg.buffer_id, msg.total_len, reason,
                      msg.table_id, msg.cookie, msg.match,
                      utils.hex_array(msg.data))
```

#### Packet-Out Message ####
Mensaje que permite inyectar paquetes desde el controlador al switch. La siguiente figura muestra que es el controlador quien lo inicia:

![PacketOut](http://flowgrammable.org/static/media/uploads/msgs/packet_out.png)

La estructura de este mensaje para la version 1.3.0 del protocolo Openflow se muestra a continuación:

![PacketOut](http://flowgrammable.org/static/media/uploads/msg_structure/packet_out_1_1.png)

La parte del API de Ryu relacionada con este mensaje se encuentra en el siguiente [enlace](https://ryu.readthedocs.io/en/latest/ofproto_v1_3_ref.html#packet-out-message). 

**Clase**

```python 
class ryu.ofproto.ofproto_v1_3_parser.OFPPacketOut(datapath, buffer_id=None, in_port=None, actions=None, data=None, actions_len=None)
```

**Ejemplo**

```python 
def send_packet_out(self, datapath, buffer_id, in_port):
    ofp = datapath.ofproto
    ofp_parser = datapath.ofproto_parser

    actions = [ofp_parser.OFPActionOutput(ofp.OFPP_FLOOD, 0)]
    req = ofp_parser.OFPPacketOut(datapath, buffer_id,
                                  in_port, actions)
    datapath.send_msg(req)
```

#### FlowMod Message ####
Este es uno de los principales mensajes pues permite al controlador modificar el estado de un switch openflow. A continuación se muestra la secuencia:

![FlowMod](http://flowgrammable.org/static/media/uploads/msgs/flow_mod_sequence.png)

La estructura de este mensaje para la version 1.3.0 del protocolo Openflow se muestra a continuación:

![FlowMod](http://flowgrammable.org/static/media/uploads/msgs/flow_mod_1_1.png)

La parte del API de Ryu relacionada con este mensaje se encuentra en el siguiente [enlace](https://ryu.readthedocs.io/en/latest/ofproto_v1_3_ref.html#ryu.ofproto.ofproto_v1_3_parser.OFPFlowMod). 

**Clase**

```python 
class ryu.ofproto.ofproto_v1_3_parser.OFPFlowMod(datapath, cookie=0, cookie_mask=0, table_id=0, command=0, idle_timeout=0, hard_timeout=0, priority=32768, buffer_id=4294967295, out_port=0, out_group=0, flags=0, match=None, instructions=None)
```

**Ejemplo**

```python 
def send_flow_mod(self, datapath):
    ofp = datapath.ofproto
    ofp_parser = datapath.ofproto_parser

    cookie = cookie_mask = 0
    table_id = 0
    idle_timeout = hard_timeout = 0
    priority = 32768
    buffer_id = ofp.OFP_NO_BUFFER
    match = ofp_parser.OFPMatch(in_port=1, eth_dst='ff:ff:ff:ff:ff:ff')
    actions = [ofp_parser.OFPActionOutput(ofp.OFPP_NORMAL, 0)]
    inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS,
                                             actions)]
    req = ofp_parser.OFPFlowMod(datapath, cookie, cookie_mask,
                                table_id, ofp.OFPFC_ADD,
                                idle_timeout, hard_timeout,
                                priority, buffer_id,
                                ofp.OFPP_ANY, ofp.OFPG_ANY,
                                ofp.OFPFF_SEND_FLOW_REM,
                                match, inst)
    datapath.send_msg(req)
```

####Estructuras importantes####
Como se mostro al principio, cada flujo de la tabla de flujos del switch tiene una estructura como la que se muestra en la siguiente figura:

[Flujo](https://www.researchgate.net/profile/Tooska_Dargahi/publication/315734989/figure/fig7/AS:667926713622534@1536257546661/OpenFlow-V100-Flow-Table-Architecture.png)

