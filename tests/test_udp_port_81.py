from test_net import TestNet
from utils import run_iperf

if __name__ == '__main__':
    net = TestNet(4)
    print("--- Test UDP port 8080 ---")

    server_host = net.hosts[0]
    client_host = net.hosts[-1]

    run_iperf("UDP", net, 10000, server_host, client_host)

    net.stop()


