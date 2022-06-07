import board,busio
from time import sleep
from adafruit_st7735r import ST7735R
import displayio

mosi_pin = board.IO35
clk_pin = board.IO36
reset_pin = board.IO38
cs_pin = board.IO34
dc_pin = board.IO37

displayio.release_displays()

spi = busio.SPI(clock=clk_pin, MOSI=mosi_pin)

display_bus = displayio.FourWire(spi, command=dc_pin, chip_select=cs_pin, reset=reset_pin)

display = ST7735R(display_bus, width=128, height=160, bgr = True)

bitmap = displayio.OnDiskBitmap("/0.bmp")
bitmap1 = displayio.OnDiskBitmap("/1.bmp")
bitmap2 = displayio.OnDiskBitmap("/2.bmp")
bitmap3 = displayio.OnDiskBitmap("/3.bmp")
group = displayio.Group()
display.show(group)

while True:
    tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)
    group.append(tile_grid)
    sleep(3)
    tile_grid = displayio.TileGrid(bitmap1, pixel_shader=bitmap.pixel_shader)
    group.append(tile_grid)
    sleep(0.1)
    tile_grid = displayio.TileGrid(bitmap2, pixel_shader=bitmap.pixel_shader)
    group.pop()
    group.append(tile_grid)
    sleep(0.1)
    tile_grid = displayio.TileGrid(bitmap3, pixel_shader=bitmap.pixel_shader)
    group.pop()
    group.append(tile_grid)
    sleep(2)