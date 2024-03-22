#!/usr/bin/env bash

# Inicializa el firewall
# Uso: firewall.sh <arch-de-reglas> <switch-bloqueante>


if [ "$1" ] && [ "$2" ]; then
    ./pox/pox.py log.level --DEBUG log.color forwarding.l2_learning firewall --rules="$1" --blocking="$2"
elif [ "$1" ]; then
    ./pox/pox.py log.level --DEBUG log.color forwarding.l2_learning firewall --rules="$1"
else
    ./pox/pox.py log.level --DEBUG log.color forwarding.l2_learning firewall
fi
