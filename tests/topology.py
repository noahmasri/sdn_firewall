from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI

import os

class CustomTopo (Topo) :
    def __init__ (self, num_switches):
        if num_switches <= 0:
            raise Exception("La cantidad de switches debe ser al menos 1")

        Topo.__init__(self)
        switches = []
        for i in range(num_switches):
            switch_name = "s{}".format(i+1)
            print(switch_name)
            switch = self.addSwitch("s{}".format(i+1))
            switches.append(switch)
            if i == 0:
                continue
            self.addLink(switches[i-1], switch)

        h1 = self.addHost('h1') 
        h2 = self.addHost('h2') 
        h3 = self.addHost('h3') 
        h4 = self.addHost('h4')

        s1 = switches[0]
        sn = switches[-1]

        self.addLink(s1, h1)
        self.addLink(s1, h2)
        self.addLink(sn, h3)
        self.addLink(sn, h4)

topos = {"customTopo": CustomTopo }
