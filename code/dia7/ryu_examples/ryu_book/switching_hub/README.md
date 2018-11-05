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
bajo nivel para la implementación de una aplicación que se ejecuta en el controlador para interactuar con la red. En el paso 1
anteriormente descrito se menciona la necesidad de importar clases y librerias base. Pero una cosa es importar y otra cosa es usar
por dicha razon es necesario conocer no solo el modelo de programacin del controlador (anteriormente mencionado) si no con que
esta este relacionado. Para el caso, este modelo esta relacionado con el protocolo Openflow, por lo tanto, el conocimiento, por lo
menos de los aspectos basicos, para conocer que elemento del protocolo esta abstrayendo una clase determinada y asi poder 
hacer uso de objetos asociados a esta para la implementación de su lógica. Esto lo podemos reducir a dos pasos:
1. Conocimiento de la especificacin Openflow a emplear ([Enlaces con diferentes especificaciones](https://www.opennetworking.org/software-defined-standards/specifications/))
2. Conocimiento del API del controlador, el cual abstrae dicha especificación ([API de Ryu](https://ryu.readthedocs.io/en/latest/index.html))

### Algunos mensajes del protocolo empleados ###
En la pagina de (flowgramable)[http://flowgrammable.org/sdn/openflow/message-layer/] se encuentran de manera resumida los diferentes mensajes Openflow. A
continuación se muestran los mas importantes y la parte del API relacionada con estos.

