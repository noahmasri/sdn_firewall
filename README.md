# Para settear la topologia
sudo mn --custom topology.py --topo customTopo,`<numero de switches>` --controller=remote,ip=127.0.0.1,port=6633

# Para correr el controlador
## Default
./pox/pox.py forwarding.l2_learning firewall

./pox.py log.level --DEBUG log.color forwarding.l2_learning firewall

## Verbose 
./pox/pox.py forwarding.l2_learning log.level --DEBUG

## firewall
./pox/pox.py firewall log.level --DEBUG