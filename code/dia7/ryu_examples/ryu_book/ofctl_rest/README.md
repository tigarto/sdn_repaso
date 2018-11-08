


## ¿Por que usar el API REST? ##
Esta API es de utilidad por que:
1. Facilita ver el estado actual de los switches concetados al controlador. 
2. Facilita la inlación manual de nuevos flujos y grupos.
3. Facilita la obtención y actualización de estadisticas.

## Recomendaciones ##

* Usar en ambiente de depuración no de produccion producción, esto por cuestiones de seguridad principalmente.
* Emplear un consumidor de la interfaz, para el caso se pueden emplear herramientas como curl y postman.

## Resumen ##

Anteriormente se mostro la capacidad para construir aplicaciones internas codificadas teniendo en cuenta el lenguaje y la interfaz de programación del controlador. El ejemplo analizado fue el **simple_switch**; en este, el controlador definia la lógica necesaria para hacer que el switch openflow se comportara como un swit tradicional. Sin embargo, en este caso, es posible que se le indique a un switch openflow la manera de funcionar (como **simple_switch** para el caso) por medio de la REST API. En el siguiente [enlace](https://ryu.readthedocs.io/en/latest/app/ofctl_rest.html#id10) se muestra como construir aplicaciones para Ryu usando el REST API. 

## Ejemplos ##

A continuación se van a experimentar los ejemplos analizando las paginas:
1. [Interactive Ryu with Postman](https://inside-openflow.com/2016/06/23/interactive-ryu-with-postman/)
2. [Built-in Ryu applications with ryu.app.ofctl_rest
](https://ryu.readthedocs.io/en/latest/app/ofctl_rest.html#id10)

Para el caso se emplearán las siguientes herramientas para consumo de la interfaz:
1. curl
2. postman

### Ejemplo 1 ###

sudo mn --topo single,3 --mac --switch ovsk --controller remote

sudo ryu-manager simple_switch.py ofctl_rest.py




http://localhost:8080/stats/switches





```JSON
{
    "1": [
        {
            "actions": [
                "OUTPUT:1"
            ],
            "idle_timeout": 0,
            "cookie": 0,
            "packet_count": 3,
            "hard_timeout": 0,
            "byte_count": 238,
            "duration_nsec": 368000000,
            "priority": 32768,
            "duration_sec": 6,
            "table_id": 0,
            "match": {
                "dl_dst": "00:00:00:00:00:01",
                "dl_src": "00:00:00:00:00:02",
                "in_port": 2
            }
        },
        {
            "actions": [
                "OUTPUT:2"
            ],
            "idle_timeout": 0,
            "cookie": 0,
            "packet_count": 2,
            "hard_timeout": 0,
            "byte_count": 140,
            "duration_nsec": 366000000,
            "priority": 32768,
            "duration_sec": 6,
            "table_id": 0,
            "match": {
                "dl_dst": "00:00:00:00:00:02",
                "dl_src": "00:00:00:00:00:01",
                "in_port": 1
            }
        },
        {
            "actions": [
                "OUTPUT:1"
            ],
            "idle_timeout": 0,
            "cookie": 0,
            "packet_count": 3,
            "hard_timeout": 0,
            "byte_count": 238,
            "duration_nsec": 347000000,
            "priority": 32768,
            "duration_sec": 6,
            "table_id": 0,
            "match": {
                "dl_dst": "00:00:00:00:00:01",
                "dl_src": "00:00:00:00:00:03",
                "in_port": 3
            }
        },
        {
            "actions": [
                "OUTPUT:3"
            ],
            "idle_timeout": 0,
            "cookie": 0,
            "packet_count": 2,
            "hard_timeout": 0,
            "byte_count": 140,
            "duration_nsec": 346000000,
            "priority": 32768,
            "duration_sec": 6,
            "table_id": 0,
            "match": {
                "dl_dst": "00:00:00:00:00:03",
                "dl_src": "00:00:00:00:00:01",
                "in_port": 1
            }
        },
        {
            "actions": [
                "OUTPUT:2"
            ],
            "idle_timeout": 0,
            "cookie": 0,
            "packet_count": 3,
            "hard_timeout": 0,
            "byte_count": 238,
            "duration_nsec": 342000000,
            "priority": 32768,
            "duration_sec": 6,
            "table_id": 0,
            "match": {
                "dl_dst": "00:00:00:00:00:02",
                "dl_src": "00:00:00:00:00:03",
                "in_port": 3
            }
        },
        {
            "actions": [
                "OUTPUT:3"
            ],
            "idle_timeout": 0,
            "cookie": 0,
            "packet_count": 2,
            "hard_timeout": 0,
            "byte_count": 140,
            "duration_nsec": 342000000,
            "priority": 32768,
            "duration_sec": 6,
            "table_id": 0,
            "match": {
                "dl_dst": "00:00:00:00:00:03",
                "dl_src": "00:00:00:00:00:02",
                "in_port": 2
            }
        }
    ]
}
```


ryu.app.ofctl_rest provides REST APIs for retrieving the switch stats and Updating the switch stats. This application helps you debug your application and get various statistics.

we can use the API to override the functionality of the learning switch.

the ryu-manager command above demonstrates the power of Ryu’s multi-component design. You can have more than one controller application running at the same time and it is often useful to code your applications so they can run independently or cooperatively with other applications. In this example, we have the simple learning L2 switch application provided by ryu.app.simple_switch and the REST API provided by ryu.app.ofctl_rest. As demonstrated earlier, you can run the switch without the API and, as we will demonstrate later, we can use the API to override the functionality of the learning switch

> Tip
> the ryu-manager command above demonstrates the power of Ryu’s multi-component design. You can have more than one controller application running at the same time and it is often useful to code your applications so they can run independently or cooperatively with other applications.

https://ryu.readthedocs.io/en/latest/app/ofctl_rest.html
https://inside-openflow.com/2016/06/23/interactive-ryu-with-postman/




**Enlaces sin organizar**

* https://mik.bme.hu/~zfaigl/QoS/doc/README.html
* https://pdfs.semanticscholar.org/e7a6/8f5b35b986902ce8cf8244c15d0950cf26e2.pdf
* http://dehesa.unex.es/bitstream/handle/10662/4417/TFMUEX_2016_Amarilla_Cardoso.pdf?sequence=1&isAllowed=y
* https://inside-openflow.com/2016/12/14/ip-reputation-mitigation-api/
* https://hal.inria.fr/hal-01539656/document
* https://www.mdpi.com/2224-2708/7/3/33/htm
* https://ecs.victoria.ac.nz/foswiki/pub/Groups/SDN/Publications/Final_Report_-_Jordan_Ansell.pdf
* https://inside-openflow.com/2016/12/14/ip-reputation-mitigation-api/
* https://sdndos.wordpress.com/
* https://www.kth.se/social/files/569421cff276546db5254b80/Final_report_CRAVED.pdf
* https://www.researchgate.net/publication/323717318_Multi-controller_Based_Software-Defined_Networking_A_Survey
* orchflow
* https://www.grotto-networking.com/SDNfun.html#basic-graph-creation-and-an-algorithm
* https://www.kth.se/social/files/569421cff276546db5254b80/Final_report_CRAVED.pdf (sobre metricas)
