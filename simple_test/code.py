# Lilygo ESP32 S2
# http://educ8s.tv/part/esp32s2


import board,busio
from time import sleep
from adafruit_st7735r import ST7735R
import displayio
import terminalio
from adafruit_display_text import label


mosi_pin = board.IO35
clk_pin = board.IO36
reset_pin = board.IO38
cs_pin = board.IO34
dc_pin = board.IO37

displayio.release_displays()

spi = busio.SPI(clock=clk_pin, MOSI=mosi_pin)

display_bus = displayio.FourWire(spi, command=dc_pin, chip_select=cs_pin, reset=reset_pin)

display = ST7735R(display_bus, width=128, height=160, bgr = True)

splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(128, 160, 1)

color_palette = displayio.Palette(1)
color_palette[0] = 0x00FF00  # Bright Green

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(118, 150, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=5, y=5)
splash.append(inner_sprite)

# Draw a label
text_group = displayio.Group(scale=1, x=11, y=24)
text = "Hello World!\n\nThis is a sample\ntext!\n\nEverything is \nworking fine."
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF)
text_group.append(text_area)  # Subgroup for text scaling
splash.append(text_group)

while True:
    pass
