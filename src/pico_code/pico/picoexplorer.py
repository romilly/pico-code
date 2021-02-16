from enum import Enum

class Button(Enum):
    BUTTON_A = 0
    BUTTON_B = 1
    BUTTON_X = 3
    BUTTON_Y = 4

class ADC(Enum):
    ADC0 = 0
    ADC1 = 1
    ADC2 = 2

class Motor(Enum):
    MOTOR1 = 0
    MOTOR2 = 1

class Motion(Enum):
    FORWARD = 0
    REVERSE = 1
    STOP = 2

class GP(Enum):
    GP0 = 0
    GP1 = 1
    GP2 = 2
    GP3 = 3
    GP4 = 4
    GP5 = 5
    GP6 = 6
    GP7 = 7

def get_width() -> int:
    pass

def get_height() -> int:
    pass

def init(buffer: bytearray) -> None:
    pass

def get_adc(adc: ADC) -> int:
    pass

def update() -> None:
    pass

def is_pressed(button: Button) -> bool:
    pass

def set_motor(motor: Motor, motion: Motion, speed: float = 0.0):
    pass

def set_pen(r: int, g: int, b: int):
    pass

def clear() -> None:
    pass

def pixel(x: int, y: int) -> None:
    pass

def text(text: str, x: int, y: int, wrap: int):
    pass



