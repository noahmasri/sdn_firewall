from pox.lib.packet import ipv4, ethernet
from pox.lib.addresses import EthAddr, IPAddr
import pox.openflow.libopenflow_01 as of 

class Rule():
    def __init__(self, rule_options):
        self.dest_port = rule_options.get('dest_port', None)
        self.origin_port = rule_options.get('origin_port', None)
        self.dest_ip = (IPAddr(rule_options['dest_ip'][0]), rule_options['dest_ip'][1]) if 'dest_ip' in rule_options else None
        self.src_ip = (IPAddr(rule_options['src_ip'][0]), rule_options['src_ip'][1]) if 'src_ip' in rule_options else None
        self.dest_mac = EthAddr(rule_options['dest_mac']) if 'dest_mac' in rule_options else None
        self.src_mac = EthAddr(rule_options['src_mac']) if 'src_mac' in rule_options else None
        self.trans_protocol = prot_from_string(rule_options.get('trans_protocol', None))

    
    # parametros_json = {'dest_port': 80, 'origin_port': 2344, 'dest_ip': '192.168.1.1', 'src_ip': '192.168.1.2'}
    # mi_objeto = MiClase(**parametros_json)
    @staticmethod
    def from_string(string):
        filters = string.split(';')
        key_values = dict(map(lambda x: split_key_val(x), filters))
        Rule(**key_values)


# dl_src	Ethernet source address
# dl_dst	Ethernet destination address
# dl_vlan	VLAN ID
# dl_vlan_pcp	VLAN priority
# dl_type	Ethertype / length (e.g. 0x0800 = IPv4)
# nw_tos	IP TOS/DS bits
# nw_proto	IP protocol (e.g., 6 = TCP) or lower 8 bits of ARP opcode
# nw_src	IP source address
# nw_dst	IP destination address
# tp_src	TCP/UDP source port
# tp_dst	TCP/UDP destination port

    def to_match(self):
        return of.ofp_match(
            tp_src=self.origin_port,
            tp_dst=self.dest_port,
            nw_dst=self.dest_ip,
            nw_src=self.src_ip,
            nw_proto=self.trans_protocol,
            dl_src=self.src_mac,
            dl_dst=self.dest_mac,
            dl_type=ethernet.IP_TYPE
        )

    def __repr__(self):
         return "{}(\n  dest_port={},\n  origin_port={},\n  dest_ip={},\n  src_ip={},\n  dest_mac={},\n  src_mac={},\n  trans_protocol={})".format(
            self.__class__.__name__,
            self.dest_port,
            self.origin_port,
            self.dest_ip,
            self.src_ip,
            self.dest_mac,
            self.src_mac,
            self.trans_protocol,
        )
        
            
def split_key_val(filter):
    splitted = filter.split('=')
    print(splitted)
    if len(splitted) != 2:
        raise Exception('Filter should contain key and value')

    return (splitted[0], splitted[1])

def prot_from_string(prot):
    if prot == "TCP":
        return ipv4.TCP_PROTOCOL
    elif prot == "UDP":
        return ipv4.UDP_PROTOCOL
    elif prot == "ICMP":
        return ipv4.ICMP_PROTOCOL
    elif prot == None:
        return None
    else:
        raise Exception("protocolo invalido")
