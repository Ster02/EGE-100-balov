import ipaddress

net = ipaddress.ip_network('45.172.106.203/255.255.252.0', 0)
k = 1

for ip in net:
    print(ip, k)
    k += 1