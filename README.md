# Para settear la topologia
sudo mn --custom topology.py --topo customTopo,`<numero de switches>` --controller=remote,ip=127.0.0.1,port=6633

# Para correr el controlador
## Default
./pox/pox.py forwarding.l2_learning firewall (opcional --rules=`<path al archivo de reglas>` --blocking_switch=`<numero de switch bloqueado>`)

## Verbose 
./pox/pox.py log.level --DEBUG log.color forwarding.l2_learning firewall

## firewall
./pox/pox.py firewall log.level --DEBUG

# POX
Dado que para correr el controlador necesitabamos de los archivos 

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

