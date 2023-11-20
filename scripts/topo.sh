#!/usr/bin/env bash

# Inicializa la topologia en mininet
# Uso: topo.sh <cant-de-switches>
# Por default se settean 4 switches

if [ "$1" ]; then
    sudo mn --custom topology.py --topo customTopo,"$1" --controller=remote,ip=127.0.0.1,port=6633
  else
    sudo mn --custom topology.py --topo customTopo,4 --controller=remote,ip=127.0.0.1,port=6633
fi

