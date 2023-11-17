from test_net import TestNet
from threading import Thread

SERVER_LIFETIME = 10

def server(host):
    res = host.cmd(f"iperf -s -u -p 5001 -t {SERVER_LIFETIME}")
    print("---- SERVER RESULT ----")
    print(res)

def client(host, server_ip):
    res = host.cmd(f"iperf -c {server_ip} -u -p 5001")
    print("---- CLIENT RESULT ----")
    print(res)


def test_communication(server_host, client_host):
    print("\n\n--- Test full block ---")
    print(f"  Server: {server_host}")
    print(f"  Client: {client_host}")

    server_handle = Thread(target=server, args=[server_host])
    client_handle = Thread(target=client, args=[client_host, server_host.IP()])

    server_handle.start()
    client_handle.start()
    
    server_handle.join()
    client_handle.join()

if __name__ == '__main__':
    net = TestNet(4)
    print("--- Test blocked pair ---")
    hosts = net.hosts

    test_communication(hosts[1], hosts[2])
    test_communication(hosts[2], hosts[1])


