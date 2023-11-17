from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
import pox.lib.util as poxutil
import json

from rules import Rule

log = core.getLogger ()

def parse_rules(rules_path):
    rules_vec = []
    if rules_path is None:
        return rules_vec

    log.debug("Reading rules file")
    
    with open(rules_path) as rules_file:
        rules = json.load(rules_file)
        for rule_line in rules:
            rule = Rule(rule_line)
            rules_vec.append(rule)
    return rules_vec


class Firewall(EventMixin):
    def __init__ (self, rules, blocking):
        if set(core.openflow.connections.keys()) < blocking:
            raise Exception("No such blocking switch")
        self.listenTo(core.openflow)
        self.rules = parse_rules(rules)
        self.blocking_switch = blocking
        log.debug(" Enabling Firewall Module ")
    
    def _handle_ConnectionUp(self, event):
        log.info("Switch %s has come up.", event.dpid)
        if event.dpid == self.blocking_switch:
            for rule in self.rules:
                msg = of.ofp_flow_mod()
                msg.match = rule.to_match()
                event.connection.send(msg)

def launch (rules = None, blocking = 1):
    log.info("Starting")
    core.registerNew(Firewall, rules, blocking)

# "pox/ext/ejemplo.json"

# ./pox/pox.py fowarding/l2_learning firewall --rules=pox/ext/ejemplo.json

