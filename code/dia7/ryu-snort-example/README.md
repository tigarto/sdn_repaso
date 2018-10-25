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

### Ejemplo de la integración de snort con ryu

Este fue tomado del siguiente [enlace](https://ryu.readthedocs.io/en/latest/snort_integrate.html)




