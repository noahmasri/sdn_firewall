from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
import json

from rules import Rule

log = core.getLogger ()

def parse_rules(path):
    rules = []
    with open(path) as rules_file:
        # rules_file = json.load(mi_json)
        for rule_line in rules_file:
            # si usasemos json: Rule(line)
            rule = Rule.from_string(rule_line)
            print(rule_line)
            rules.append(of.ofp_match(rule))
    return rules


class Firewall(EventMixin):
    def __init__ ( self, rules_path, blocking_switch):
        self.listenTo(core.openflow)
        self.rules = [Rule.from_string("dest_port=10;src_port=40;trans_protocol=TCP")]
        #self.rules = parse_rules(rules_path)
        self.blocking_switch = blocking_switch
        log.debug(" Enabling Firewall Module ")
    
    def _handle_ConnectionUp(self, event):
        log.info("Switch %s has come up.", event.dpid)
        if event.dpid == self.blocking_switch:
            for rule in self.rules:
                msg = of.ofp_flow_mod()
                msg.match = rule.to_match()
                
                event.connection.send(msg)

    
    def _handle_PacketIn (self, event):
        packet = event.parsed
        #log.info("Paquete del tipo %s enviado", packet.type)  

def launch (rules_path = "", blocking_switch = 1):
    log.info("Starting")
    core.registerNew(Firewall, rules_path, blocking_switch)


# ./pox/pox.py fowarding/l2_learning firewall --rules_path = None --

