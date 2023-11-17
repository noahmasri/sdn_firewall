from test_net import TestNet
from threading import Thread

SERVER_LIFETIME = 10

def server(host):
    res = host.cmd(f"iperf -s -u -p 5001 -t {SERVER_LIFETIME}")
    print("\n\n---- SERVER RESULT ----")
    print(res)

def client(host, server_ip):
    res = host.cmd(f"iperf -c {server_ip} -u -p 5001")
    print("\n\n---- CLIENT RESULT ----")
    print(res)


if __name__ == '__main__':
    net = TestNet(4)
    print("--- Test UDP + src_port + src_ip ---")

    hosts = net.hosts
    server_handle = Thread(target=server, args=[hosts[-1]])
    client_handle = Thread(target=client, args=[hosts[0], hosts[-1].IP()])

    server_handle.start()
    client_handle.start()
    
    server_handle.join()
    client_handle.join()


