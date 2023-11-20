from test_net import TestNet

from utils import run_iperf


if __name__ == '__main__':
    net = TestNet(4)
    print("--- Test blocked pair ---")
    hosts = net.hosts

    host_2 = hosts[1]
    host_3 = hosts[2]

    run_iperf("UDP", net, 5001, host_2, host_3)
    run_iperf("UDP", net, 5001, host_3, host_2)

    print("--- Test funciona para otros pares ---")

    run_iperf("UDP", net, 5001, host_2, hosts[-1])


