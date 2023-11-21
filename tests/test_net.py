import sys
import os

from topology import CustomTopo
from mininet.node import RemoteController
from mininet.net import Mininet
from mininet.util import dumpNodeConnections

class TestNet(Mininet):
    def __init__(self, switches=1):
        topo = CustomTopo(switches)
        controller = RemoteController(name='c0', ip='127.0.0.1', port=6633)
        super().__init__(topo=topo, controller=controller)
        super().start()
