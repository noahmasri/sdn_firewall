# Para settear la topologia
sudo mn --custom topology.py --topo customTopo,`<numero de switches>` --controller=remote,ip=127.0.0.1,port=6633

# Para correr el controlador
## Default
./pox/pox.py forwarding.l2_learning firewall [--rules=`<path al archivo de reglas>`] [--blocking_switch=`<numero de switch bloqueado>`]

## Verbose 
./pox/pox.py log.level --DEBUG log.color forwarding.l2_learning firewall [--rules=`<path al archivo de reglas>`] [--blocking_switch=`<numero de switch bloqueado>`]

# POX
Dado que para correr el controlador necesitabamos del codigo fuente de POX, clonamos su repositorio dentro de nuestra carpeta, y todo lo correspondiente a nuestro firewall, siguiendo con la informacion otorgada por el README de pox, se encuentra en la carpeta pox/ext. El codigo fue tomado de la pagina [ Repositorio POX](https://github.com/noxrepo/pox).

# IPerf
Comandos a usar:
-u usar UDP
-c modo cliente, -s modo servidor 
-i intervalo entre reportes
-p puerto (default es 5201)

## Para correr el servidor:
Servidor: iperf -s -u -i 1

## Para correr el cliente:
Cliente:  iperf -c 10.0.0.x -p y --cport z
x: numero de host
y: numero de puerto donde escucha host servidor
z: numero de puerto del cliente

