import board,busio
from time import sleep
from adafruit_st7735r import ST7735R
import displayio

mosi_pin = board.GP11
clk_pin = board.GP10
reset_pin = board.GP17
cs_pin = board.GP18
dc_pin = board.GP16

displayio.release_displays()

spi = busio.SPI(clock=clk_pin, MOSI=mosi_pin)

display_bus = displayio.FourWire(spi, command=dc_pin, chip_select=cs_pin, reset=reset_pin)

display = ST7735R(display_bus, width=128, height=160, bgr = True)

bitmap = displayio.OnDiskBitmap("/0.bmp")
bitmap1 = displayio.OnDiskBitmap("/1.bmp")
bitmap2 = displayio.OnDiskBitmap("/2.bmp")
bitmap3 = displayio.OnDiskBitmap("/3.bmp")
bitmap4 = displayio.OnDiskBitmap("/4.bmp")
group = displayio.Group()
display.show(group)

while True:
    tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)
    group.append(tile_grid)
    sleep(1)
    tile_grid = displayio.TileGrid(bitmap1, pixel_shader=bitmap.pixel_shader)
    group.append(tile_grid)
    sleep(2)
    tile_grid = displayio.TileGrid(bitmap2, pixel_shader=bitmap.pixel_shader)
    group.pop()
    group.append(tile_grid)
    sleep(0.1)
    tile_grid = displayio.TileGrid(bitmap3, pixel_shader=bitmap.pixel_shader)
    group.pop()
    group.append(tile_grid)
    sleep(0.1)
    tile_grid = displayio.TileGrid(bitmap4, pixel_shader=bitmap.pixel_shader)
    group.pop()
    group.append(tile_grid)
    sleep(2)