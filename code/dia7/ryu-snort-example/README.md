# SNORT + RYU

## Instalación de snort
Se siguió el documento [Snort 2.9.9.x on Ubuntu 14 and 16](https://bit.ly/2EKk2Mx) 

### Instalación de los prerrequisitos de snort

```
sudo apt-get install -y build-essential
sudo apt-get install -y libpcap-dev libpcre3-dev libdumbnet-dev
sudo apt-get install -y bison flex
mkdir ~/snort_src
cd ~/snort_src
wget https://snort.org/downloads/snort/daq-2.0.6.tar.gz
tar -xvzf daq-2.0.6.tar.gz
cd daq-2.0.6
./configure
make
sudo make install
```

### Instalación de snort como tal

```
sudo apt-get install -y zlib1g-dev liblzma-dev openssl libssl-dev
sudo apt-get install -y libnghttp2-dev
cd ~/snort_src
wget https://www.snort.org/downloads/archive/snort/snort-2.9.9.0.tar.gz
tar -xvzf snort-2.9.9.0.tar.gz
cd snort-2.9.9.0
./configure --enable-sourcefire
make
sudo make install
```

### Chequeando la instalación

```
tigarto@fuck-pc:~/snort_src/snort-2.9.9.0$ snort -V

   ,,_     -*> Snort! <*-
  o"  )~   Version 2.9.9.0 GRE (Build 56) 
   ''''    By Martin Roesch & The Snort Team: http://www.snort.org/contact#team
           Copyright (C) 2014-2016 Cisco and/or its affiliates. All rights reserved.
           Copyright (C) 1998-2013 Sourcefire, Inc., et al.
           Using libpcap version 1.7.4
           Using PCRE version: 8.38 2015-11-23
           Using ZLIB version: 1.2.8
```

## Ejemplo de la integración de snort con ryu

Este fue tomado del siguiente [enlace](https://ryu.readthedocs.io/en/latest/snort_integrate.html). En la siguiente figura tomada del enlace [Ryu with Snort Integration](http://linton.tw/2014/09/03/Ryu-with-Snort-Integration/)

PONER FIGURA

### Configuración del snort

Los archivos asociados son:
* simple_switch_snort.py.
* pigrelay.py 

Inicialmente se siguen las instrucciónes dadas en el siguiente [enlace](https://ryu.readthedocs.io/en/latest/snort_integrate.html) con el fin de crear reglas y configurar el snort despues de que este ha sido instalado:

```
cd /etc/snort/rules
gedit 
sudo gedit Myrules.rules & 
```

El contenido del archivo creado (**Myrules.rules**) se muestra a continuacion:

```
alert icmp any any -> any any (msg:"Pinging...";sid:1000004;)
alert tcp any any -> any 80 (msg:"Port 80 is accessing"; sid:1000003;)
```

Luego se edita el archivo **snort.conf** mediante el siguiente comando:

```
sudo gedit /etc/snort/snort.conf
```

Para lo cual se agrega la siguiente linea:

```
...
include $RULE_PATH/Myrules.rules
...
```

### Pruebas iniciales

Se ingresa al directorio de trabajo donde estan los codigos fuente:

```
cd $DIRECTORIO_DE_TRABAJO
```

Ahora se siguien los siguientes pasos:
1. Se arranca el controlador:

```
sudo ryu-manager simple_switch_snort.py
```

2. Se arranca la topologia de test:

```
sudo mn --controller=remote,ip=127.0.0.1,port=6633 --switch ovs,protocols=OpenFlow13 --topo single,2
```

3. Se define el port mirror para el snort

```
sudo ifconfig s1-eth2 promisc
sudo snort -i s1-eth2 -A unsock -l /tmp -c /etc/snort/snort.conf  # Ver anexo 1
```

Para el último de los anteriores comandos ver el **anexo 1** si se presentan problemas:

4. Se ejecuta el script que enviara los eventos del snort al controlador (por lo menos eso creo???)

```
sudo python pigrelay.py
```

A continuacion se muestra el estado de ejecución hasta el momento:

PONER FIGURA

Vamos a proceder a realizar un ping en mininet:

```
h1 ping -c 2 h2
```

La siguiente figura muestra el resultado:

PONER FIGURA

Las salidas se muestran a continuación:

**Salida del controlador**

```

tigarto@fuck-pc:~/Documents/tesis_2018-2/sdn_repaso/code/dia7/ryu-snort-example$ sudo ryu-manager simple_switch_snort.py
loading app simple_switch_snort.py
loading app ryu.controller.ofp_handler
instantiating app None of SnortLib
creating context snortlib
instantiating app simple_switch_snort.py of SimpleSwitchSnort
[snort][INFO] {'port': 51234, 'unixsock': False}
instantiating app ryu.controller.ofp_handler of OFPHandler
[snort][INFO] Network socket server start listening...
[snort][INFO] Connected with 127.0.0.1
alertmsg: Pinging...
ethernet(dst='33:33:00:00:00:02',ethertype=34525,src='4a:75:8e:3d:7d:14')
alertmsg: ICMP PING *NIX
icmp(code=0,csum=11822,data=echo(data=array('B', [194, 86, 209, 91, 0, 0, 0, 0, 37, 226, 0, 0, 0, 0, 0, 0, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]),id=20841,seq=1),type=8)
ipv4(csum=63245,dst='10.0.0.2',flags=2,header_length=5,identification=12185,offset=0,option=None,proto=1,src='10.0.0.1',tos=0,total_length=84,ttl=64,version=4)
ethernet(dst='4a:75:8e:3d:7d:14',ethertype=2048,src='c6:72:9d:de:04:12')
alertmsg: Pinging...
icmp(code=0,csum=11822,data=echo(data=array('B', [194, 86, 209, 91, 0, 0, 0, 0, 37, 226, 0, 0, 0, 0, 0, 0, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]),id=20841,seq=1),type=8)
ipv4(csum=63245,dst='10.0.0.2',flags=2,header_length=5,identification=12185,offset=0,option=None,proto=1,src='10.0.0.1',tos=0,total_length=84,ttl=64,version=4)
ethernet(dst='4a:75:8e:3d:7d:14',ethertype=2048,src='c6:72:9d:de:04:12')
alertmsg: ICMP PING
icmp(code=0,csum=11822,data=echo(data=array('B', [194, 86, 209, 91, 0, 0, 0, 0, 37, 226, 0, 0, 0, 0, 0, 0, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]),id=20841,seq=1),type=8)
ipv4(csum=63245,dst='10.0.0.2',flags=2,header_length=5,identification=12185,offset=0,option=None,proto=1,src='10.0.0.1',tos=0,total_length=84,ttl=64,version=4)
ethernet(dst='4a:75:8e:3d:7d:14',ethertype=2048,src='c6:72:9d:de:04:12')
alertmsg: Pinging...
icmp(code=0,csum=13870,data=echo(data=array('B', [194, 86, 209, 91, 0, 0, 0, 0, 37, 226, 0, 0, 0, 0, 0, 0, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]),id=20841,seq=1),type=0)
ipv4(csum=4082,dst='10.0.0.1',flags=0,header_length=5,identification=22197,offset=0,option=None,proto=1,src='10.0.0.2',tos=0,total_length=84,ttl=64,version=4)
ethernet(dst='c6:72:9d:de:04:12',ethertype=2048,src='4a:75:8e:3d:7d:14')
alertmsg: ICMP Echo Reply
icmp(code=0,csum=13870,data=echo(data=array('B', [194, 86, 209, 91, 0, 0, 0, 0, 37, 226, 0, 0, 0, 0, 0, 0, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]),id=20841,seq=1),type=0)
ipv4(csum=4082,dst='10.0.0.1',flags=0,header_length=5,identification=22197,offset=0,option=None,proto=1,src='10.0.0.2',tos=0,total_length=84,ttl=64,version=4)
ethernet(dst='c6:72:9d:de:04:12',ethertype=2048,src='4a:75:8e:3d:7d:14')
alertmsg: ICMP PING *NIX
icmp(code=0,csum=54822,data=echo(data=array('B', [195, 86, 209, 91, 0, 0, 0, 0, 124, 232, 0, 0, 0, 0, 0, 0, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]),id=20841,seq=2),type=8)
ipv4(csum=63185,dst='10.0.0.2',flags=2,header_length=5,identification=12245,offset=0,option=None,proto=1,src='10.0.0.1',tos=0,total_length=84,ttl=64,version=4)
ethernet(dst='4a:75:8e:3d:7d:14',ethertype=2048,src='c6:72:9d:de:04:12')
alertmsg: Pinging...
icmp(code=0,csum=54822,data=echo(data=array('B', [195, 86, 209, 91, 0, 0, 0, 0, 124, 232, 0, 0, 0, 0, 0, 0, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]),id=20841,seq=2),type=8)
ipv4(csum=63185,dst='10.0.0.2',flags=2,header_length=5,identification=12245,offset=0,option=None,proto=1,src='10.0.0.1',tos=0,total_length=84,ttl=64,version=4)
ethernet(dst='4a:75:8e:3d:7d:14',ethertype=2048,src='c6:72:9d:de:04:12')
alertmsg: ICMP PING
icmp(code=0,csum=54822,data=echo(data=array('B', [195, 86, 209, 91, 0, 0, 0, 0, 124, 232, 0, 0, 0, 0, 0, 0, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]),id=20841,seq=2),type=8)
ipv4(csum=63185,dst='10.0.0.2',flags=2,header_length=5,identification=12245,offset=0,option=None,proto=1,src='10.0.0.1',tos=0,total_length=84,ttl=64,version=4)
ethernet(dst='4a:75:8e:3d:7d:14',ethertype=2048,src='c6:72:9d:de:04:12')
alertmsg: Pinging...
icmp(code=0,csum=56870,data=echo(data=array('B', [195, 86, 209, 91, 0, 0, 0, 0, 124, 232, 0, 0, 0, 0, 0, 0, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]),id=20841,seq=2),type=0)
ipv4(csum=3937,dst='10.0.0.1',flags=0,header_length=5,identification=22342,offset=0,option=None,proto=1,src='10.0.0.2',tos=0,total_length=84,ttl=64,version=4)
ethernet(dst='c6:72:9d:de:04:12',ethertype=2048,src='4a:75:8e:3d:7d:14')
alertmsg: ICMP Echo Reply
icmp(code=0,csum=56870,data=echo(data=array('B', [195, 86, 209, 91, 0, 0, 0, 0, 124, 232, 0, 0, 0, 0, 0, 0, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]),id=20841,seq=2),type=0)
ipv4(csum=3937,dst='10.0.0.1',flags=0,header_length=5,identification=22342,offset=0,option=None,proto=1,src='10.0.0.2',tos=0,total_length=84,ttl=64,version=4)
ethernet(dst='c6:72:9d:de:04:12',ethertype=2048,src='4a:75:8e:3d:7d:14')
alertmsg: Pinging...
ethernet(dst='33:33:00:00:00:02',ethertype=34525,src='e6:df:a5:df:11:90')
alertmsg: Pinging...
ethernet(dst='33:33:00:00:00:02',ethertype=34525,src='c6:72:9d:de:04:12')
alertmsg: Pinging...
ethernet(dst='33:33:00:00:00:02',ethertype=34525,src='4a:75:8e:3d:7d:14')
alertmsg: Pinging...
ethernet(dst='33:33:00:00:00:02',ethertype=34525,src='c6:72:9d:de:04:12')
alertmsg: Pinging...
ethernet(dst='33:33:00:00:00:02',ethertype=34525,src='e6:df:a5:df:11:90')
alertmsg: Pinging...
ethernet(dst='33:33:00:00:00:02',ethertype=34525,src='4a:75:8e:3d:7d:14')
```

**Salida en la consola de pigrelay**

```
sudo python pigrelay.py
INFO:__main__:Unix Domain Socket listening...
INFO:__main__:Start the network socket client....
INFO:__main__:Send the alert messages to Ryu.
INFO:__main__:Send the alert messages to Ryu.
INFO:__main__:Send the alert messages to Ryu.
INFO:__main__:Send the alert messages to Ryu.
INFO:__main__:Send the alert messages to Ryu.
INFO:__main__:Send the alert messages to Ryu.
INFO:__main__:Send the alert messages to Ryu.
INFO:__main__:Send the alert messages to Ryu.
INFO:__main__:Send the alert messages to Ryu.
INFO:__main__:Send the alert messages to Ryu.
INFO:__main__:Send the alert messages to Ryu.
INFO:__main__:Send the alert messages to Ryu.
INFO:__main__:Send the alert messages to Ryu.
INFO:__main__:Send the alert messages to Ryu.
INFO:__main__:Send the alert messages to Ryu.
INFO:__main__:Send the alert messages to Ryu.
INFO:__main__:Send the alert messages to Ryu.

```

## Anexos

### Anexo 1

Puede suceder que al ejecutarse el comando:

```
sudo snort -i s1-eth2 -A unsock -l /tmp -c /etc/snort/snort.conf
```

Aparezca el siguiente problema: 

```
...
   alert_fragments: INACTIVE
    alert_large_fragments: INACTIVE
    alert_incomplete: INACTIVE
    alert_multiple_requests: INACTIVE
ERROR size 1248 != 1120
ERROR: Failed to initialize dynamic preprocessor: SF_DCERPC2 version 1.0.3 (-2)
Fatal Error, Quitting..
```

Para solucionarlo seguir los pasos que se encuentran en el enlace [How to fix Snort dynamic preprocessor loading error
](http://wikisecure.net/how-to-fix-snort-dynamic-preprocessor-error/) 

### Anexo 2

A veces la ejecución de ejecución de Ryu junto con mininet pone problemas, por lo menos en nuestro caso concreto, cuando no se cambia en mininet el puerto de trabajo a 6633 y se deja que se trabaje en el puerto por default del Ryu (6653). A continuación se coloca el caso contado:

Inicialmente se ejecutan los comandos que llaman a mininet y al controlador Ryu:

```
sudo mn
sudo ryu-manager simple_switch.py
```

En caso de que pase un error cuando se arranca el controlador, es necesario ejecutar los siguientes comandos:

```
sudo fuser -k 6653/tcp
sudo ryu-manager simple_switch.py
```



