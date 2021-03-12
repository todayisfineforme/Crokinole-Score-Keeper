from machine import Pin, I2C, Timer
import utime
from ssd1306 import SSD1306_I2C
import framebuf

WIDTH = 128
HEIGHT = 64

i2c=machine.I2C(0)

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

button_1 = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)
button_2 = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
button_3 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
button_4 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
button_small = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_up)

team1=0
team2=0

def changescore1up():
    global team1
    oled.fill_rect(15,20,25,15,0)
    team1 += 5
    oled.text(str(team1),15,20)
    
def changescore2up():
    global team2
    oled.fill_rect(95,20,25,15,0)
    team2 += 5
    oled.text(str(team2),95,20)
    
def changescore1down():
    global team1
    oled.fill_rect(15,20,25,15,0)
    team1 -= 5
    oled.text(str(team1),15,20)
    
def changescore2down():
    global team2
    oled.fill_rect(95,20,25,15,0)
    team2 -= 5
    oled.text(str(team2),95,20)

while True:
    oled.text('Crokinole', 25, 0)
    oled.text('team 1', 0, 9)
    oled.text('team 2', 80, 9)
    oled.hline(0,16,48,1)
    oled.hline(80,16,50,1)
    oled.text(str(team1),15,20)
    oled.text(str(team2),95,20)
    oled.show()
    
    if button_1.value() == 0:
        changescore1down()
        utime.sleep(0.25)
        
    if button_2.value() == 0:
        changescore1up()
        utime.sleep(0.25)

    if button_3.value() == 0:
        changescore2down()
        utime.sleep(0.25)

    if button_4.value() == 0:
        changescore2up()
        utime.sleep(0.25)

#     for i in range (0, 164):
#         oled.scroll(1,0)
#         oled.show()
#         utime.sleep(0.01)
