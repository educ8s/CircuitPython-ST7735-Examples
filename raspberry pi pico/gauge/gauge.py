#Library from https://github.com/benevpi/Circuit-Python-Gauge
#I just fixed one error and a warning

from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.rect import Rect
from adafruit_display_text.label import Label
import terminalio
import displayio
import math

class Gauge(displayio.Group):
    def __init__(self, min_val, max_val, width, height, base_size=8, 
                 colour=0x0000FF, outline_colour=0x0000FF, outline = True, bg_colour=0000000, display_value=True, 
                 value_label="", arc_colour=0xFF0000, colour_fade=False):
        super().__init__()
        self.pivot1=[(width//2)-(base_size//2), 0]
        self.pivot2=[(width//2)+(base_size//2), 0]
        self.mid=width//2
        self.min_val = min_val
        self.max_val = max_val
        self.colour = colour
        self.height = height
        self.value_label=value_label
        self.outline_colour=outline_colour
        self.outline = outline

        self.length = int(1.4*(width/2))
        if outline: self.arrow = Triangle(self.pivot1[0],self.length, self.pivot2[0], self.length, self.mid,
                     0, fill=self.colour, outline=self.outline_colour)
        else: self.arrow = Triangle(self.pivot1[0],self.length, self.pivot2[0], self.length, self.mid,
                     0, fill=self.colour)
                     
        self.data = Label(terminalio.FONT, text="0.0", color=0xFFFFFF)
        self.data.x = width//2
        self.data.y = (height - self.length)//2
        if display_value: super().append(self.data)

        arc = draw_arc(width//2,self.height, self.length, 0, width, 10, arc_colour, 
                        height, colour_fade=colour_fade)
        for tri in arc: super().append(tri)
        super().append(self.arrow)

    def update(self, val):
        max_angle = 135
        if val<self.min_val: angle = 45
        elif val> self.max_val: angle = max_angle
        else:
            angle = ((((val-self.min_val)/(self.max_val-self.min_val)))*
                    (max_angle-45)+45)

        top_point_x = self.mid-int(math.cos(math.radians(angle))*self.length)
        top_point_y = int(math.sin(math.radians(angle))*self.length)

        if self.outline: self.arrow = Triangle(self.pivot1[0],self.height, self.pivot2[0], self.height, top_point_x,
                     self.height-top_point_y, fill=self.colour, outline=self.outline_colour)
        else: self.arrow = Triangle(self.pivot1[0],self.height, self.pivot2[0], self.height, top_point_x,
                     self.height-top_point_y, fill=self.colour)
        super().pop()
        super().append(self.arrow)
        
        #need a better way of formatting this
        #and maybe shifting it to the right place here.
        self.data.text = self.value_label+str(int(val))

def draw_arc(centerpoint_x, centerpoint_y, length, start_x, end_x, num_sections, 
            colour, height, colour_fade=False):
    triangles = []
    lastpoint = [start_x, int(math.sqrt(length*length-(centerpoint_x-start_x)*(centerpoint_x-start_x)))]
    increment = (end_x - start_x) / num_sections
    counter = 0
    for i in range(0,num_sections):
        if colour_fade: this_colour=colour[counter]
        else: this_colour = colour
        next_x = start_x + (i+1)*increment
        nextpoint = [int(next_x), int(math.sqrt(length*length - (centerpoint_x-next_x)*(centerpoint_x-next_x)
                    ))]
        triangles.append(Triangle(lastpoint[0], height-lastpoint[1], lastpoint[0], 
                        height-lastpoint[1], nextpoint[0],height-nextpoint[1], outline=this_colour))
        lastpoint = nextpoint
        counter = counter+1
    return triangles