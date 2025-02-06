from RPLCD.i2c import CharLCD

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)
#lcd.clear()

#lcd.write_string('Hello, World!')

import smbus
import time
import socket
#import I2C_LCD_driver

# Funkcja do pobrania adresu IP
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('10.254.254.254', 1))  # Próba połączenia
        ip = s.getsockname()[0]
    except Exception:
        ip = 'Nie znaleziono'
    finally:
        s.close()
    return ip

# Inicjalizacja wyświetlacza LCD
#lcd = I2C_LCD_driver.LCD()

# Pobranie adresu IP
ip = get_ip_address()

# Wyświetlanie adresu IP na LCD
lcd.write_string(ip)
#lcd.lcd_clear()
#lcd.lcd_display_string("Adres IP:", 1)
#lcd.lcd_display_string(ip, 2)

# Czekaj przez 10 sekund, aby zobaczyć wynik
#time.sleep(10)
#lcd.lcd_clear()

