# Apuntes de repaso

# Dia 4

## Fecha: 31/07/2018

> **Preguntas y actividades en torno a las cuales gira este guion**
> 1. ¿Como se puede hacer snifing de codigo?, explorar herramientas: wireshark, scapy?, etc,...
> 2. Como implementar lo que se he hecho en R con python. 
> 3. Como implementar estadisticas de utilidad para analisis de trafico.


## Desarrollo de las actividades

### Actividad 1 - Herramientas de snnifing ###

A continuacion se muestran algunas herramientas para hacer sniffing:
* tcpdump
* Wireshark
* tshark (Wireshark in terminal)
* EtherApe
* Kismet
* EtherApe
* NetworkMiner

### Actividad 2 - Lo que se tenia con R ###
Para empezar a realizar un analisis muy informal se tomo inicialmente una traza (syn_attack.pcap) de internet del siguiente [enlace](https://github.com/ctfs/write-ups-2013/tree/master/pico-ctf-2013/ddos-detection) de un ataque de sincronizacion. Luego, para su posterior analisis se emplearon los siguientes archivos de R:
1. [script_analisis.R](code/dia5/code_R/script_analisis.R) que lee el archivo pcap guardando algunas tablas sencillas. Asi mismo cuenta el numero de paquetes por segundo y los grafica. A continuación se muestran los comandos usados para escribir:

```
write.csv(pcap_capture_info,"pcap_capture_info.csv")
write.csv(pcap_capture_ip,"pcap_capture_ip.csv")
write.csv(pcap_capture_tcp,"pcap_capture_tcp.csv")
write.csv(pcap_capture_IPs,"pcap_capture_IPs.csv")
write.csv(pcap_capture_info,"pcap_capture_info.csv")
write.csv(pairs,"pairs.csv")
write.csv(nodes,"nodes.csv")
write.csv(ips,"ips.csv")
```

Los archivos resultantes del analisis anterior se encuentran en el siguente [enlace](code/dia5/code_R/info_syn_attack)

2. [r_notebook.Rmd](code/dia5/code_R/notebooks/r_notebook.Rmd) es un notebook en R que permite realizar el analisis del archivo pcap ya mencionado. En el siguiente [directorio](code/dia5/code_R/info2_syn_attack) se encuentran las imagenes asociadas a este archivo de analisis.

¿Que estaditicas podria trabajar?
http://library.iugaza.edu.ps/thesis/116507.pdf

**tcpdump**
Enlaces utiles:
https://hackertarget.com/tcpdump-examples/
https://danielmiessler.com/study/tcpdump/
https://www.tecmint.com/12-tcpdump-commands-a-network-sniffer-tool


http://packetlife.net/media/library/12/tcpdump.pdf
https://www.sans.org/security-resources/tcpip.pdf
http://taviso.decsystem.org/files/tcpdump_quickref.pdf
https://www.garykessler.net/library/tcpip_prg_GKA.pdf
http://alumni.cs.ucr.edu/~marios/ethereal-tcpdump.pdf





**Algunas trazas disponibles**:
syn_attack.pcap -> https://github.com/ctfs/write-ups-2013/tree/master/pico-ctf-2013/ddos-detection, http://shell-storm.org/repo/CTF/PicoCTF-2013/DDoS%20Detection:%2085/

Informacion teorica: http://web2.uwindsor.ca/courses/cs/aggarwal/cs60564/Assignment1/Won.pdf (tratar de imitir este montaje).




Instalacion de R studio en Ubuntu:
se llevaron a cabo las siguientes instrucciones: https://medium.com/@GalarnykMichael/install-r-and-rstudio-on-ubuntu-12-04-14-04-16-04-b6b3107f7779

Instalacion de librerias:
1. libcrafter: A high level C++ network packet sniffing and crafting library (https://github.com/pellegre/libcrafter)
2. crafter: An R package to work with PCAPs (https://github.com/hrbrmstr/crafter)



Capturas de internet para analisis: 
- ¿How to analyse pcap files?
- The most important params to analyses pcaps.
- statistical analysis of pcap files.

1. Wireshark: https://wiki.wireshark.org/SampleCaptures
2. Stratosphere: https://www.stratosphereips.org/datasets-overview/ -- Mirar medidas que pueden tomar estos IPS
 
---

library(crafter)
library(dplyr)
library(ggplot2)
library(igraph)

pcap_capture <- read_pcap("syn_attack.pcap")
pcap_capture_info <- pcap_capture$packet_info()
pcap_capture_ip <- pcap_capture$get_layer("IP")
pcap_capture_tcp <- pcap_capture$get_layer("TCP")
pcap_capture_IPs <- pcap_capture$get_ips("all")
# Pares
pairs <- count(pcap_capture_ip, src, dst, protocol_name)
# Nodos
nodes <- unique(c(pairs$src, pairs$dst))
# Grafo
g <- graph_from_data_frame(pairs, directed=TRUE, vertices=nodes)
# Obtencion de las IPs involucradas
ips <- unique(c(pcap_capture_ip$src,pcap_capture_ip$dst));
cont_rangos <- table(cut(pcap_capture_info$packet_size, c(0,20,40,80,160,320,640,1280,2560), 
                         include.lowest=TRUE);
print(cont_rangos);
start_time = pcap_capture_ip$tv_sec[1] + pcap_capture_ip$tv_usec[1]/1e6;
t = (pcap_capture_ip$tv_sec + pcap_capture_ip$tv_usec/1e6) - start_time;
time_divs = seq(0, max(t)+1, by=0.5);
cont_pack_seg = table(cut(t,time_divs, 
                      include.lowest=TRUE));
nom_filas=rownames(cont_pack_seg);

valores = as.vector(cont_pack_seg);
plot(time_divs[c(0:length(valores))],valores,type="l",
     col="blue",main="Conteo de paquetes",xlab = "t",ylab="Paquetes/segundo")

---

library(crafter)


http_pcap <- read_pcap("/home/tigarto/Documents/datasets/http.cap")

# get overall capture summary
summary(http_pcap)
# same think
http_pcap$summary()



Columnas:
1. num     
2. tv_sec 
3. tv_usec 
4. layer_count 
5. protocols                                           
6. packet_size

# high level packet info
http_pcap_info <- http_pcap$packet_info()
head(http_pcap_info)

# retrieve specific layers
http_pcap_ip <- http_pcap$get_layer("IP")
head(http_pcap_ip)


http_pcap_tcp <- http_pcap$get_layer("TCP")
head(http_pcap_tcp)

# http_pcap_udp <- http_pcap$get_layer("UDP") --> ERROR
# head(http_pcap_udp) --> ERROR

# get the IPs from the capture
http_pcap_IPs <- http_pcap$get_ips("all")

http_pcap_pay_12 <- http_pcap$get_payload(12) --> ???
http_pcap_pay_13 <- http_pcap$get_payload(13)
http_pcap_pay_14 <- http_pcap$get_payload(14)
http_pcap_pay_15 <- http_pcap$get_payload(15)
http_pcap_pay_16 <- http_pcap$get_payload(16)

head(http_pcap$packet_info(), 15)
http_pcap$packet_info()$packet_size


# have some semi-useless fun!
pairs <- count(http_pcap_ip, src, dst, protocol_name)


nodes <- unique(c(pairs$src, pairs$dst))
g <- graph_from_data_frame(pairs, directed=TRUE, vertices=nodes)

plot(g, layout=layout.circle, vertex.size=sqrt(degree(g)), 
     vertex.label=NA, edge.width=0.5, edge.arrow.width=0.5, edge.arrow.size=0.5)

---

tcpdump -qns 0 -A -r blah.pcap

tcpdump -qns 0 -X -r serverfault_request.pcap

tshark -r file.pcap -V

For example: to see the traffic between hosts A and B, I use:

tcpdump -r <pcapfile> -n host A or host B

Mirar la posiilidad de usar tshark.

tcpdump -r somepkgs.pcap udp
tcpdump -r somepkgs.pcap ip





https://github.com/yandex/tcplanz
https://github.com/vgrichina/httpdump



https://github.com/devopsmonster/packetscanner


https://github.com/search?l=Shell&p=2&q=tcpdump&type=Repositories
https://github.com/d4rkcat/Spoofr
https://github.com/DanielSchwartz1/tcpdump
https://github.com/appropriate/docker-tcpdump


http://www.fukuda-lab.org/mawilab/v1.1/2016/06/18/20160618.html
////////// Ver: https://github.com/ctfs/write-ups-2013/tree/master/pico-ctf-2013/ddos-detection

http://shell-storm.org/repo/CTF/PicoCTF-2013/DDoS%20Detection:%2085/pbm.txt

http://shell-storm.org/repo/CTF/PicoCTF-2013/DDoS%20Detection:%2085/


---

Reportes base
https://docs.google.com/document/d/1rsJXiC8nDYuWYBuwnNZrFOJQBXxXP_xDGT1Cb8gdnT8/edit
https://docs.google.com/document/d/1O3a19sTv1Ij1P8wBlslGf8aetiN6HhErAkqSFWWiOZU/edit

Archivos pcap (para analizar):
https://drive.google.com/drive/u/0/folders/1XB5GW7-G9BzuR_LZxVYZA96xm9s2WA-K?ogsrc=32
