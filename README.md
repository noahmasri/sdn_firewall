# Trabajo practico 2: SDN
## Para settear la topologia
```bash
sudo mn --custom topology.py --topo customTopo,`<numero de switches>` --controller=remote,ip=127.0.0.1,port=6633
```
## Para correr el controlador
### Default
Para correr el comando normalmente:
```bash
./pox/pox.py forwarding.l2_learning firewall [--rules=<arch-de-reglas>] [--blocking_switch=`<switch-bloqueante>`]
```
Para correr el comando usando scripts
### Para otorgar permisos de ejecuccion:
```bash
chmod +x ./scripts/*
```
```bash
./scripts/firewall.sh `<path al archivo de reglas>``<numero de switch bloqueado>`
```

### Verbose 
```bash
./pox/pox.py log.level --DEBUG log.color forwarding.l2_learning firewall [--rules=`<path al archivo de reglas>`] [--blocking_switch=`<numero de switch bloqueado>`]
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
Servidor: iperf -s -u -i 1

## Para correr el cliente:
Cliente:  iperf -c 10.0.0.x -p y --cport z
x: numero de host
y: numero de puerto donde escucha host servidor
z: numero de puerto del cliente

## Para correr las pruebas
En la carpeta tests, estan los distintos casos a verificar de la catedra, estas son:
* `test_h2_h3_blocked.py`: Test de comunicacion entre un par arbitrario de hosts (h2 y h3)
* `test_tcp_port_80`: Test de comunicacion entre cliente y servidor en puerto 80 utilizando el protocolo TCP
* `test_udp_port_80`: Test de comunicacion entre cliente y servidor en puerto 80 utilizando el protocolo UDP
* `test_udp_port_10000`: Test de comunicacion entre cliente y servidor en puerto 10000 utilizando el protocolo UDP (deberian llegar los paquetes)
* `test_udp_dst_port_ip`: Test de comunicacion entre cliente h1 (10.0.0.1) y servidor en puerto 5001 utilizando el protocolo UDP

Para ejecutar estas pruebas, primero se tiene que levantar el controlador POX y ejecutar el test elegido utilizando `sudo python3 <nombre_de_test>`

## Para ejecutar scripts
`./scripts/<nombre_de_script>`

Si hay errores de permisos:
* `chmod +x scripts/<nombre_de_script>` y ejecutar como fue mencionado anteriormente
* `sudo bash scripts/<nombre_de_script>`