# Traffic Monitor #

##  Objetivo ##

Comprender como usar Openflow para adquirir información estadistica de la red.

## Importancia de conocer las estadisticas de la red ##

A continuación se describen algunos de los aspectos por los cuales es necesario conocer las estadisticas asociadas a la red:
1. Permiten detectar las causas de un error en la red tan rapido como sea posible para acelerar su solucion.
2. Permite monitorear la red para ver que esta se encuentre en condiciones de funcionamiento normales.

## Conociendo estructuras y mensajes asociados a las estadisticas ##

Para hablar de las estructuras asociadas a las estadisticas observemos el siguiente grafico (visto anteriormente):

![openflow](https://camo.githubusercontent.com/cb42aaf6fc2e87e7d87ae16db0d20087a57dfe0f/68747470733a2f2f7777772e7265736561726368676174652e6e65742f70726f66696c652f546f6f736b615f446172676168692f7075626c69636174696f6e2f3331353733343938392f6669677572652f666967372f41533a36363739323637313336323235333440313533363235373534363636312f4f70656e466c6f772d563130302d466c6f772d5461626c652d4172636869746563747572652e706e67)

La parte que se va a explorar para este caso es la parte asociada al campo counters que es el correspondiente a todas las estadisticas.

### Mensajes ###

#### StatsReq Message ####

Este mensaje es la manera que tiene el switch de enviar un paquete capturado al controlador. Hay dos razones por las cuales esto paso; por la existencia de una accion explicita como el resultado de un matching para este comportamiento, o desde un miss en la parte del match de las tablas, o un error de ttl. En la siguiente figura se muestra que es el switch quien lo inicia:

![StatsReq](http://flowgrammable.org/static/media/uploads/seq/stats_req_seq.png)

La parte del **body** asociada al mensaje cambia segun las estadisticas en particular solicitadas. Veamos esto para dos casos particulares;
la obtencion de las estadisticas de flujos y la obtencion de estadisticas de un puerto.

##### Estadistcas de un flujo #####

La estructura del body cuando lo que se solicita son las estadisticas de flujos se muestra en la siguiente figura:

![StatsReq](http://flowgrammable.org/static/media/uploads/msgs/stats/stats_req_flow_1_1.png)

La parte del API de Ryu relacionada esta estructura se encuentra en el siguiente [enlace](https://ryu.readthedocs.io/en/latest/ofproto_v1_3_ref.html#ryu.ofproto.ofproto_v1_3_parser.OFPFlowStatsRequest). 

**Clase **

```python 
class ryu.ofproto.ofproto_v1_3_parser.OFPFlowStatsRequest(datapath, flags=0, table_id=255, out_port=4294967295, out_group=4294967295, cookie=0, cookie_mask=0, match=None, type_=None)```

**Ejemplo**

```python 
def send_flow_stats_request(self, datapath):
    ofp = datapath.ofproto
    ofp_parser = datapath.ofproto_parser

    cookie = cookie_mask = 0
    match = ofp_parser.OFPMatch(in_port=1)
    req = ofp_parser.OFPFlowStatsRequest(datapath, 0,
                                         ofp.OFPTT_ALL,
                                         ofp.OFPP_ANY, ofp.OFPG_ANY,
                                         cookie, cookie_mask,
                                         match)
    datapath.send_msg(req)
```

##### Estadistcas de un de puerto #####

La estructura del body cuando lo que se solicita son las estadisticas de puertos se muestra en la siguiente figura:

![StatsReq](http://flowgrammable.org/static/media/uploads/msgs/stats/stats_req_port_1_1.png)

La parte del API de Ryu relacionada esta estructura se encuentra en el siguiente [enlace](https://ryu.readthedocs.io/en/latest/ofproto_v1_3_ref.html#ryu.ofproto.ofproto_v1_3_parser.OFPPortStatsRequest). 

**Clase **

```python 
class ryu.ofproto.ofproto_v1_3_parser.OFPPortStatsRequest(datapath, flags=0, port_no=4294967295, type_=None)
```

**Ejemplo**

```python 
def send_port_stats_request(self, datapath):
    ofp = datapath.ofproto
    ofp_parser = datapath.ofproto_parser

    req = ofp_parser.OFPPortStatsRequest(datapath, 0, ofp.OFPP_ANY)
    datapath.send_msg(req)
```



* https://www.slideshare.net/joelwking/introduction-to-openflow-41257742

