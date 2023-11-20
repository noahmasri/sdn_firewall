from test_net import TestNet
from utils import run_iperf


if __name__ == '__main__':
    net = TestNet(4)
    print("--- Test UDP + src_port + src_ip ---")

    hosts = net.hosts

    server_host = hosts[0]
    client_host = hosts[-1]

    run_iperf("UDP", net, 5001, server_host, client_host)

