# Apuntes de repaso

# Dia 4

## Fecha: 27/07/2018

> **Preguntas y actividades en torno a las cuales gira este guiin**
> 1. ¿Que se tiene en lo que respecta a los ataques de denegación de servicio? - Recopilación de material viejo.
> 2. Retomar una clasificacion de los tipos de ataques DoS buscando restringir 
> 3. Mirar que herramientas se tienen para lanzar ataques DoS.
> 4. Describir el caso de uso copiado de internet. El objetivo es mostrar los pasos para ponerlo en marca y los pasos que se tuvieron en cuenta en algun momento para realizar medidiones. 

## Desarrollo de las actividades

### Actividad 1 - Reproducción del ataque de smallko empleando containernet ###

En esta sección lo que se tratará es intentar reproducir el ataque DoS mostrado en la pagina de smallko: [Denial of Service Attack](http://csie.nqu.edu.tw/smallko/sdn/dos_attack.htm). El ataque se reproducira empleando containernet, sin embargo en su base va a ser exactamente igual. 

**Elementos**:
Los archivos asociados a esta parte se encuentran en el siguiente [enlace](code/dia4/dia4_dos_example). A continuación se describen cada uno de estos brevemente:
1. **Dockerfile**: Archivo que describe los elementos de la imagen **ubuntu-test** usada en la topologia mininet:([Dockerfile](code/dia4/dia4_dos_example/Dockerfile))
2. **symple_containernet_topo**: Archivo que describe la topologia de la red que conecta los contenedores: h1 (cliente), h2 (atacante) y h3 (victima): ([symple_containernet_topo.py](code/dia4/dia4_dos_example/symple_containernet_topo.py))
3. **home_server/index.html**: Codigo con el index asociado al servidor web: ([index.html](code/dia4/dia4_dos_example/home_server/index.html))
4. **dos_code/attack.py**: Codigo empleado para llevar a cabo el ataque: ([attack.py](code/dia4/dia4_dos_example/dos_code/attack.py))

**Supocisiones**:
1. Los contenedores empleados en la topologia ya se han construido a partir de las imagenes. Un comando de contruccion sera de la forma mostrada a continuacion:

```
sudo docker build -t ubuntu-test .
```

2. A veces es necesario aplicar el siguiente comando de emergencia cuando una instancia renuente de un controlador ocupa un puerto que se necesita: ```sudo fuser -k 6633/tcp```

**Pasos**:


1. **Arrancar la topologia y probar conectividad**:

```
sudo python symple_containernet_topo.py
```


2. **Arrancar el controlador**:

```
./pox.py log.level --DEBUG openflow.of_01 --port=6653 forwarding.l2_learning 
```

Una vez se arranca probar conectividad en mininet:

```
containernet> pingall
*** Ping: testing ping reachability
h1 -> h2 h3 
h2 -> h1 h3 
h3 -> h1 h2 
*** Results: 0% dropped (6/6 received)
```

Luego dentro del contenedor asociado al servidor (h3) hacer lo siguiente:
1. **Iniciar el servidor web**:

```
** Consola containernet **
xterm h3
----
** Consola h3 **
root@h3:~# cd /mnt/home_server/

root@h3:/mnt/home_server# ls
index.html

root@h3:/mnt/home_server# python -m SimpleHTTPServer
Serving HTTP on 0.0.0.0 port 8000 ...
```

Verificar que se vea la pagina web. Para el caso se empleo wget desde el contenedor h1:

```
** Consola containernet **
xterm h1
----
** Consola h3 **
root@h1:/# cd tmp/
root@h1:/tmp# wget http://10.0.0.253:8000/index.html
--2018-07-27 21:34:56--  http://10.0.0.253:8000/index.html
Connecting to 10.0.0.253:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 158 [text/html]
Saving to: 'index.html'

index.html          100%[===================>]     158  --.-KB/s    in 0s      

2018-07-27 21:34:56 (15.8 MB/s) - 'index.html' saved [158/158]

root@h1:/tmp# ls 
index.html
```

Si se tiene curl instalado otro test puede hacerse con el comando:

```
curl 10.0.0.253:8000
```

Desde uno de los clientes:

4. **Poniendo un sniffer**: Esto se hace con el proposito de analizar capturas de trafico:

```
sudo wireshark &
```

5. **Lanzar el ataque**:

```
root@h2:/mnt/dos_code# cd /mnt/dos_code/

root@h2:/mnt/dos_code# ls
attack.py

python attack.py -t 20 -c 100 http://10.0.0.253
```

Una vez lanzado el ataque se vera que el servidor se revienta no pudiendo responder a peticiones curl desde un cliente. Por otro lado tambien se nota que el controlador se empieza a inundar de trafico de modo que este tambien sufrira.

Para un analisis posterior desde el punto de vista estadistico se hicieron dos capturas de trafico dentro de la carpeta [capturas](code/dia4/dia4_dos_example):
1. **dos_atack1.pcap**: Se lanzo el ataque, el servidor se revienta y el envio de paquetes openflow se dispara, se presume que debido a esto el controlador corre el riesgo de inundarse ante tanta peticion hecha desde el switch.
2. **dos_non_atack.pcap**: no se lanzo el ataque, solo se lanzaron pings y curl. Despues del segundo ping ya al parecer no se registraban flujos (algo mediandamente esperado), sin embargo, cada vez que se hacia una peticion curl se registraban flujos, no se por que la verdad.

**Por ahora luego**
1- si el canal entre la interfaz del controlador y el switch no es privado, como se monitorea el gtrafico openflow.
2- como sacar estadisticas empleando python -> hacer el notebook.
3- Mirar otro ataque.
4- Mirar como enviar paquetes pcap.
5- Volver a hacer trazas pcap.


# Hecho de afan --- Aplazado para otro dia --- Pasar a otro readme #

http://sdnhub.org/tutorials/onos/
https://wiki.onosproject.org/display/ONOS/A+Beginner%27s+Guide+to+Contribution
https://www.youtube.com/watch?v=l25Ukkmk6Sk
https://github.com/chunhai/sdn_ONOS_CORD/wiki/Build-and-debug-a-new-project-of-ONOS
https://github.com/chunhai/sdn_ONOS_CORD/wiki/Build-and-debug-a-new-project-of-ONOS
http://www.maojianwei.com/2015/11/24/ONOS-in-Practice-for-Share-one-Project-Set-up-Debug-Hot-Deployment/
https://wiki.onosproject.org/display/ONOS12/Debugging+ONOS+with+IntelliJ+IDEA


https://groups.google.com/a/onosproject.org/forum/#!topic/onos-dev/hdPpdf7e1ck


**A tener en cuenta**:
* En IDEs se descargo el InteliJ. Fala instalarlo.

**Enlace importante**: https://wiki.onosproject.org/display/ONOS/Developer+Guide
Otra parte donde tambien se habla de esto esta en: https://wiki.onosproject.org/display/test/Building+ONOS


**Instalando prerequisitos**

```
sudo apt install maven

sudo apt-get install software-properties-common -y && \
sudo add-apt-repository ppa:webupd8team/java -y && \
sudo apt-get update && \
echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | sudo debconf-set-selections && \
sudo apt-get install oracle-java8-installer oracle-java8-set-default -y
```

**Download ONOS code & Build ONOS**

```
cd ~
git clone https://gerrit.onosproject.org/onos
cd onos
export ONOS_ROOT=$(pwd)
tools/build/onos-buck build onos --show-output
```

**Run ONOS**  (-- Apenas vamos aca)

```
tools/build/onos-buck run onos-local -- clean debug  # 'clean' to delete all previous running status; 'debug' to enable Remote Debug function
```