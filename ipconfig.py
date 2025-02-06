import os

ip = os.system(ip -4 a | grep -o '(?<=inet\s)\d+(\.\d+){3}')
ipc=[]
ipc.append(ip.strip(' '))

print(ip)