from test_net import TestNet
from threading import Thread

SERVER_LIFETIME = 20

def protocol_to_flag(protocol):
    if protocol == "TCP":
        return ""
    elif protocol == "UDP":
        return "-u"

    raise Exception("Protocol must be TCP or UDP") 

def server(host, protocol, port):
    res = host.cmd(f"iperf -s {protocol_to_flag(protocol)} -p {port} -t {SERVER_LIFETIME}")
    print("---- SERVER RESULT ----")
    print(res)

def client(host, server_ip, protocol, port):
    res = host.cmd(f"iperf -c {server_ip} {protocol_to_flag(protocol)} -p {port}")
    print("---- CLIENT RESULT ----")
    print(res)

def run_iperf(protocol, port, server_host, client_host):
    print(f"\n\n--- Test {protocol} ---")
    server_handle = Thread(target=server, args=[server_host, protocol, port])
    client_handle = Thread(target=client, args=[client_host, server_host.IP(), protocol, port])

    server_handle.start()
    client_handle.start()
    
    server_handle.join()
    client_handle.join()
