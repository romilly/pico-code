# Physical Computing with Graphics on Pico Explorer
# Tony Goodhew 30th Jan 2021
# 10K Ohm potentiometer on ADC0
# LED with 470 Ohm resistor on GP4
import picoexplorer as display
import utime, random, math
from machine import Pin
width = display.get_width()
height = display.get_height()
display_buffer = bytearray(width * height * 2)
display.init(display_buffer)
led = Pin(4, Pin.IN,Pin.PULL_DOWN)
# Set the backlight to 30%
# display.set_backlight(0.3)
def blk():
    display.set_pen(0,0,0)
    display.clear()
    display.update()
    
def title(msg,r,g,b):
    blk()
    display.set_pen(r,g,b)
    display.text(msg, 20, 70, 200, 4)
    display.update()
    utime.sleep(2)
    blk()
    
def horiz(l,t,r):    # left, right, top
    n = r-l+1        # Horizontal line
    for i in range(n):
        display.pixel(l + i, t)

def vert(l,t,b):   # left, top, bottom
    n = b-t+1      # Vertical line
    for i in range(n):
        display.pixel(l, t+i)

def box(l,t,r,b):  # left, top, right, bottom
    horiz(l,t,r)   # Hollow rectangle
    horiz(l,b,r)
    vert(l,t,b)
    vert(r,t,b)

def line(x,y,xx,yy): # (x,y) to (xx,yy)
    if x > xx:
        t = x  # Swap co-ordinates if necessary
        x = xx
        xx = t
        t = y
        y = yy
        yy = t
    if xx-x == 0:  # Avoid div by zero if vertical
        vert(x,min(y,yy),max(y,yy))
    else:          # Draw line one dot at a time L to R
        n=xx-x+1
        grad = float((yy-y)/(xx-x))  # Calculate gradient
        for i in range(n):
            y3 = y + int(grad * i)
            display.pixel(x+i,y3)  # One dot at a time

def show(tt):
    display.update()
    utime.sleep(tt)

def align(n, max_chars):
    # Aligns string of n in max_chars
    msg1 = str(n)
    space = max_chars - len(msg1)
    msg2 = ""
    for m in range(space):
        msg2 = msg2 +" "
    msg2 = msg2 + msg1
    return msg2  # String - ready for display

def ring(cx,cy,rr): # Centre and radius
    display.circle(cx,cy,rr)
    display.set_pen(0,0,0) # background colour
    display.circle(cx,cy,rr-1)
    
def ring2(cx,cy,r):   # Centre (x,y), radius
    for angle in range(0, 90, 2):  # 0 to 90 degrees in 2s
        y3=int(r*math.sin(math.radians(angle)))
        x3=int(r*math.cos(math.radians(angle)))
        display.pixel(cx-x3,cy+y3)  # 4 quadrants
        display.pixel(cx-x3,cy-y3)
        display.pixel(cx+x3,cy+y3)
        display.pixel(cx+x3,cy-y3)

def showgraph(v):   # Bar graph
    display.set_pen(255,0,0)
    display.text("V", 8, 50, 240, 3)
    display.set_pen(0,0,0)        # Blank old bar graph
    display.rectangle(29, 50, 220, 16)
    display.set_pen(200,200,0)    # New  bar graph
    display.rectangle(29, 50, v, 15)
    display.set_pen(255,255,255)  # Base line zero
    vert(28, 46, 68)             
    display.set_pen(0,0,255)      # percentage
    display.text(str(align(v,4)) + " %", 140, 48, 240, 3)

# Define special 5x8 characters - 8 bytes each - 0...7
# Bytes top to bottom, 5 least significant bits only
smiley = [0x00,0x0A,0x00,0x04,0x11,0x0E,0x00,0x00]
sad = [0x00,0x0A,0x00,0x04,0x00,0x0E,0x11,0x00]
heart = [0,0,0,10,31,14,4,0]
b_heart = [0,10,31,0,0,14,4,0]
up_arrow =[0,4,14,21,4,4,0,0]
down_arrow = [0,4,4,21,14,4,0,0]
bits = [128,64,32,16,8,4,2,1]  # Powers of 2

def mychar2(xpos, ypos, pattern):  # Print defined character
    for line in range(8):       # 5x8 characters
        for ii in range(5):     # Low value bits only
            i = ii + 3
            dot = pattern[line] & bits[i]  # Extract bit
            if dot:  # Only print WHITE dots
                display.pixel(xpos+i*2, ypos+line*2)
                display.pixel(xpos+i*2, ypos+line*2+1)
                display.pixel(xpos+i*2+1, ypos+line*2)
                display.pixel(xpos+i*2+1, ypos+line*2+1)
                
def mychar3(xpos, ypos, pattern):  # Print defined character
    for line in range(8):       # 5x8 characters
        for ii in range(5):     # Low value bits only
            i = ii + 3
            dot = pattern[line] & bits[i]  # Extract bit
            if dot:  # Only print WHITE dots
                display.pixel(xpos+i*3, ypos+line*3)
                display.pixel(xpos+i*3, ypos+line*3+1)
                display.pixel(xpos+i*3, ypos+line*3+2)
                display.pixel(xpos+i*3+1, ypos+line*3)
                display.pixel(xpos+i*3+1, ypos+line*3+1)
                display.pixel(xpos+i*3+1, ypos+line*3+2)
                display.pixel(xpos+i*3+2, ypos+line*3)
                display.pixel(xpos+i*3+2, ypos+line*3+1)
                display.pixel(xpos+i*3+2, ypos+line*3+2)
# ==== Main ====
title("Pimoroni Pico Explorer Workout",200,200,0)
# === Basics ===
title("Basics",200,0,0)
display.set_pen(255,255,0)
line(10,10,100,100)
show(0.25)
display.set_pen(255,0,255)
line(10,100,100,10)
show(0.25)
display.set_pen(0,255,255)
box(0,105,100,205)
show(0.25)
display.set_pen(255,0,0)
ring(160,50,50)
show(0.25)
display.set_pen(0,0,255)
ring2(160,160,50)
show(0.25)
display.text("Tony Goodhew", 15, 220, 240, 3)  
display.update()
mychar2(20, 130, up_arrow)    # Defined characters
mychar2(40, 130, smiley)      
mychar2(60, 130, heart)
mychar2(20, 160, down_arrow)  
mychar2(40, 160, sad) 
mychar2(60, 160, b_heart)
mychar3(120, 130, up_arrow)   # Bigger
mychar3(140, 130, smiley)      
mychar3(160, 130, heart)
mychar3(120, 160, down_arrow)  
mychar3(140, 160, sad) 
mychar3(160, 160, b_heart)
show(3)

# Character Set - No lower case!
title("Character set",200,200,0)
display.set_pen(0,200,0)
display.text("Character Set", 15, 15, 200, 2)
s = ""
count = 0
for i in range(32,128,8):
    for j in range(0,8,1):
        p = i + j
        if ((p < 97) or (p>122)):
            s = s + chr(p)
            count = count + 1
            if (count)/16 == int((count)/16):
                s = s +" "  # 'space' for text wrap
print(s)
display.set_pen(200,200,0)
display.text(s, 15, 40, 200, 2)
display.set_pen(0,0,200)
display.text("No lower case", 140, 110, 200, 1)
display.set_pen(200,0,0)
display.text("Size 3", 15, 130, 200, 3)
display.set_pen(0,0,200)
display.text("Size 4", 15, 156, 200, 4)
display.set_pen(0,200,0)
display.text("Size 6", 15, 190, 200, 6)
display.update()
utime.sleep(5)

# Lines demo
title("lines",200,0,0)                  
for step in range(18, 2, -5):
    blk()
    display.set_pen(0,0,0)    
    display.clear()
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue =random.randint(0, 255)
    display.set_pen(red, green, blue)
    x = 0  # Block 1
    y = 0
    x2 = 239
    for y2 in range(0,240, step):
        line(x, y, x2, y2)
        display.update()
    x = 0  # Block 2
    y = 239
    x2 = 239
    for y2 in range(239,-1,-step):
        line(x, y, x2, y2)
        display.update()
    x = 239  # Block 3
    y = 0
    x2 = 0
    for y2 in range(0,240, step):
        line(x, y, x2, y2)
        display.update()
    x = 239  # Block 4
    y = 239
    x2 = 0
    for y2 in range(239,-1,-step):
        line(x, y, x2, y2)
        display.update()
    utime.sleep(0.5)

# === Sin & Cos graphs ====
title("Drawing graphs",0,200,0)
factor = 361 /240
#sine = []
display.set_pen(80,80,80)
horiz(0,60,239)    
display.update()
display.set_pen(200,0,0)
for x in range(0,240):
    y = int ((math.sin(math.radians(x * factor)))* -50) + 60
#    sine.append(y)
    display.pixel(x,y)
    display.update()
display.text("Sine", 40, 70, 200, 2)
display.update()

display.set_pen(80,80,80)
horiz(0,180,239)    
display.update()
display.set_pen(0,200,0)
for x in range(0,240):
    y = int((math.cos(math.radians(x * factor)))* -50) + 180
    display.pixel(x,y)
display.text("Cosine", 90, 160, 200, 2)
display.update()
utime.sleep(3)

title("Text on a path",0,0,200)
# Text on a downward slant
display.set_pen(255,0,0)
msg =" Pimoroni pico explorer"
b = bytes(msg, 'utf-8')
for i in range(len(b)):
    c = b[i]
    display.character(c, i*10,i*5 +110,2)
    display.update()

# Text on a Sin wave
factor = 361 /240
display.set_pen(0,255,0)
for i in range(len(b)):
    y = int ((math.sin(math.radians(i*10 * factor)))* -50) + 60
    c = b[i]
    display.character(c, i*10,y +10,2)
    display.update()
utime.sleep(3)

title("Scrolling text on a Sine Curve",0,0,200)
# Scrolling on a Sine curve
# Modified from a method by Tony DiCola for a SSD1306
msg = 'Scrolling text on a sine curve using a pico explorer!'
f_width  = 13   # Font width in pixels
f_height = 10   # Font Height in pixels
amp = 100   # Amplitude of sin wave
freq = 1    # Screen cycles (360 degrees)
   
pos = width  # X position of the first character in the msg.
msg_len_px = len(msg) * f_width  # Pixel width of the msg.
# Extra wide lookup table - calculate once to speed things up
y_table = [0] * (width+f_width) # 1 character extra
for i in range(len(y_table)):
    p = i / (width-1)  # Compute current  position along
    # lookup table in 0 to 1 range.
    # Get y co-ordinate from table
    y_table[i] = int(((amp/2.0) * math.sin(2.0*math.pi*freq*p)) + (amp/2.0))
    
# Scrolling loop:
blk()
running = True
while running:
    # Clear scroll area
    display.set_pen(0,0,0) 
    display.rectangle(0, 50, 240, 200)
    display.set_pen(200,200,0)
    # Start again if msg finished
    pos -= 1
    if pos <= -msg_len_px:
        pos = width
    # Go through each character in the msg.

    for i in range(len(msg)):
        char = msg[i]
        char_x = pos + (i * f_width)  # Character's X position on the screen.
        if -f_width <= char_x < width:
            # If haracter is visible, draw it.
            display.text(char, char_x + 5, y_table[char_x+f_width]+60,2)
    display.set_pen(100,100,100)
    display.text("Press button Y to halt", 5, 215, 230, 2)
    display.update()
    if display.is_pressed(3): # Y button is pressed ?
        running = False
    utime.sleep(0.01)
blk()

# Physical Computing: Potentiometer, LED PWM and Bar Graph
potentiometer = machine.ADC(26) # 10K Ohm pot on ADC0
led = machine.PWM(machine.Pin(4)) # LED with 470 Ohm resistor on GP4
led.freq(1000)
led.duty_u16(0) # Switch LED OFF
title("Physical computing with graphics",0,0,200)
running = True
display.set_pen(255,255,255)
display.text("Turn Potentiometer", 20, 15, 230, 2)
display.set_pen(100,100,100)
display.text("Press button Y to halt", 5, 215, 230, 2)
display.set_pen(0,100,0)
box(60,80,180,200)
while running:    
    pot_raw = potentiometer.read_u16()
    pot = pot_raw/256
    # Adjust end values: 0 & 255
    pot = int(pot * 256.0 /255.0) - 1
    if pot > 255:
        pot = 255
#    print(pot) # Check pot's range is 0 -> 255 inclusive
    percent = int(100 * pot / 255)
    showgraph(percent)
    display.update()
    duty = pot_raw - 300 # duty must not go negative
    if duty < 0 :
        duty = 0
    led.duty_u16(duty)
    display.set_pen(pot,pot,pot) # grey to white
    display.circle(120,140,50)
    if display.is_pressed(3): # Y button is pressed ?
        running = False
        
# Tidy up
led.duty_u16(0)   # LED off
led = Pin(4, Pin.IN, Pin.PULL_DOWN) # Normal state
blk()        
display.set_pen(200,0,0)
display.text("All Done!", 55, 140, 200, 3)
display.update()
utime.sleep(2)
blk()

