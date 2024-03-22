from test_net import TestNet
from utils import run_iperf

if __name__ == '__main__':
    net = TestNet(4)
    print("--- Test TCP port 80 ---")

    server_host = net.hosts[0]
    client_host = net.hosts[-1]

    run_iperf("TCP", 80, server_host, client_host)

    net.stop()


