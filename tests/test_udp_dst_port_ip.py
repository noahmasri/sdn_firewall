from test_net import TestNet
from utils import run_iperf


if __name__ == '__main__':
    net = TestNet(4)
    print("--- Test UDP + dest_port + src_ip ---")

    hosts = net.hosts

    server_host = hosts[-1]
    client_host = hosts[0]

    run_iperf("UDP", 5001, server_host, client_host)

    net.stop()

