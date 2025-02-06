import time
import board
import busio
import netifaces
from adafruit_ssd1306 import SSD1306_I2C

import os

i2c = busio.I2C(board.SCL, board.SDA)
oled = SSD1306_I2C(128, 32, i2c, addr=27)

def get_ip_address():
    interfaces = netifaces.interfaces()
    for iface in interfaces:
        if iface != "lo":
            addrs = netifaces.ifaddresses(iface).get(netifaces.AF_INET)
            if addres:
                return addrs[0]['addr']
    return "no IP"


while True:
    #ip = get_ip_address()
    ip = os.popen("ip -4 a | grep -oP '(?<=inet\\s)\\d+(\\.\\d+){3}'").read().strip().split()[1]
    oled.fill(0)
    oled.text("IP address:", 0, 0, 1)
    oled.text(ip, 0, 10, 1)
    oled.show()
    time.sleep(10)