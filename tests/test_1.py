from test_net import TestNet
from threading import Thread

SERVER_LIFETIME = 20

def protocol_to_flag(protocol):
    if protocol == "TCP":
        return ""
    elif protocol == "UDP":
        return "-u"

    raise Exception("Protocol must be TCP or UDP") 

def server(host, protocol):
    res = host.cmd(f"iperf -s {protocol_to_flag(protocol)} -p 80 -t {SERVER_LIFETIME}")
    print("---- SERVER RESULT ----")
    print(res)

def client(host, server_ip, protocol):
    res = host.cmd(f"iperf -c {server_ip} {protocol_to_flag(protocol)} -p 80")
    print("---- CLIENT RESULT ----")
    print(res)

def run_iperf(protocol):
    print(f"\n\n--- Test {protocol} ---")
    hosts = net.hosts
    server_handle = Thread(target=server, args=[hosts[0], protocol])
    client_handle = Thread(target=client, args=[hosts[-1], hosts[0].IP(), protocol])

    server_handle.start()
    client_handle.start()
    
    server_handle.join()
    client_handle.join()


if __name__ == '__main__':
    net = TestNet(4)
    print("--- Test port 80 ---")

    run_iperf("TCP")
    run_iperf("UDP")


