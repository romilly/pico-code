# Code for *Raspberry Pi Pico Projects*
*(book currently under construction!)*

Code in the `src/pi` folder runs under Python 3 on a Raspberry Pi or other computer connected to a 
Raspberry Pi Pico running MicroPython or CircuitPython.

The `src/pico` folder contains code for the Pico.

The first program is a sender that uses PySerial to send commands from the Pi to the Pico and read the result.

To run it,
1. Run `pip3 install pyserial`.
1. Copy `sender.py` into a directory of your choice.
1. In that directory, run `python3` to start an interactive session.
1. In the session, type `send`

If all is well, this will send '2 + 2' to the Pico and print the result.
