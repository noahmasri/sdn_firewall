# Trabajo practico 2: SDN
## Scripts
Se generaron scripts para facilitar la corrida de los ejecutables. Se da al usuario la posibilidad de usarlos, y la opción de correrlos normalmente. En caso de querer usar los scripts, es necesario otorgar los permisos, o correrlos de una forma distinta a la especificada.

### Para otorgar permisos de ejecuccion:
```bash
chmod +x scripts/*
```

### Para ejecutar sin permisos:
```bash 
sudo bash scripts/<nombre_de_script>
```
## Para settear la topologia
Para correr el comando normalmente:
```bash
sudo mn --custom topology.py --topo customTopo,<cant-de-switches> --controller=remote,ip=127.0.0.1,port=6633
```
Para correr el comando usando scripts:
```bash
./scripts/topo.sh <cant-de-switches>
```
## Para correr el controlador
### Default
Para correr el comando normalmente:
```bash
./pox/pox.py forwarding.l2_learning firewall [--rules=<arch-de-reglas>] [--blocking=<nro-switch-bloqueante>]
```
Para correr el comando usando scripts
```bash
./scripts/firewall.sh [--rules=<arch-de-reglas>] [--blocking=<nro-switch-bloqueante>]
```

### Verbose 
```bash
./pox/pox.py log.level --DEBUG log.color forwarding.l2_learning firewall [--rules=<arch-de-reglas>] [--blocking=<nro-switch-bloqueante>]
```

## POX
Dado que para correr el controlador necesitabamos del codigo fuente de POX, clonamos su repositorio dentro de nuestra carpeta, y todo lo correspondiente a nuestro firewall, siguiendo con la informacion otorgada por el README de pox, se encuentra en la carpeta pox/ext. El codigo fue tomado de la pagina [ Repositorio POX](https://github.com/noxrepo/pox).

## IPerf
Comandos a usar:\
-u usar UDP\
-c modo cliente, -s modo servidor  
-i intervalo entre reportes \
-p puerto (default es 5201)

## Para correr el servidor:
Servidor: `iperf -s -u -i 1`

## Para correr el cliente:
Cliente:  `iperf -c 10.0.0.x -p y`\
x: numero de host\
y: numero de puerto donde escucha el host servidor

## Para correr las pruebas
En la carpeta tests, estan los distintos casos a verificar de la catedra, estas son:
* `test_h2_h3_blocked.py`: Test de comunicacion entre un par arbitrario de hosts (h2 y h3)
* `test_tcp_port_80`: Test de comunicacion entre cliente y servidor en puerto 80 utilizando el protocolo TCP
* `test_udp_port_80`: Test de comunicacion entre cliente y servidor en puerto 80 utilizando el protocolo UDP
* `test_udp_port_10000`: Test de comunicacion entre cliente y servidor en puerto 10000 utilizando el protocolo UDP (deberian llegar los paquetes)
* `test_udp_dst_port_ip`: Test de comunicacion entre cliente h1 (10.0.0.1) y servidor en puerto 5001 utilizando el protocolo UDP

Para ejecutar estas pruebas, primero se tiene que levantar el controlador POX y ejecutar el test elegido utilizando `sudo python3 <nombre_de_test>`

Se aplican al firewall las reglas otorgadas en la consigna, en donde:
* se deben descartar todos los paquetes cuyo host de destino sea el 80.
* se deben descartar todos los mensajes que provengan del host 1, tengan como puerto destino el 5001, y esten utilizando el protocolo UDP.
* Se debe elegir dos hosts cualquiera (en este caso, h2 y h3), y los mismos no deben poder comunicarse de ninguna forma.