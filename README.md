# Code for *Raspberry Pi Pico Projects*
*(book currently under construction!)*

Code in the `src/pi` folder runs under Python 3 on a Raspberry Pi or other computer connected to a 
Raspberry Pi Pico running MicroPython or CircuitPython.

The `src/pico` folder will eventually contain code for the Pico.

The first program is a sender that uses PySerial to send commands from the Pi to the Pico and read the result.

To run it,
1. run `pip3 install pyserial`
1. copy `sender.py` and `repl.py` into a directory of your choice
1. in that directory, run `python3 repl.py`

If all is well, this will send '2 + 2' to the Pico and print the result.
