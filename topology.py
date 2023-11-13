from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
import os

class CustomTopo ( Topo ) :
    def __init__ (self, num_switches):
        Topo.__init__(self)
        switches = []
        for i in range(num_switches):
            switch = self.addSwitch(f"s{i}")
            switches.append(switch)
            if i == 0:
                continue
            self.addLink(switches[i-1], switch)

        h0 = self.addHost('host_0') 
        h1 = self.addHost('host_1') 
        h2 = self.addHost('host_2') 
        h3 = self.addHost('host_3')

        s1 = switches[0]
        sn = switches[-1]

        self.addLink(s1, h0)
        self.addLink(s1, h1)
        self.addLink(sn, h2)
        self.addLink(sn, h3)

topos = {"customTopo": CustomTopo }