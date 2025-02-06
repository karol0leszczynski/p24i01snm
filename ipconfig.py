import os
ip = os.popen("ip -4 a | grep -oP '(?<=inet\\s)\\d+(\\.\\d+){3}'").read().strip().split()[1]
print(ip)
