from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from collections import namedtuple

log = core.getLogger ()

class Firewall(EventMixin):
    def __init__ ( self ):
        self.listenTo(core.openflow)
        core.openflow.addListeners(self)
        core.openflow.addListenerByName("PacketIn", self._handle_PacketIn )
        log.debug(" Enabling Firewall Module ")
    
    # def _handle_ConnectionUp(self, event):
    #     self.connections.add(event.connection)
    #     self.install_flow(event.connection)
    #     log.info("Switch %s has come up.", event.dpid)  
    
    def _handle_PacketIn (self, event):
        packet = event.parsed
        log.info("Paquete del tipo %s enviado", packet.type)  

def launch ():
    log.info("Starting")
    core.registerNew(Firewall)


# ./pox/pox.py fowarding/l2_learning firewall

