#  Remote control of the Pico

You'll find instructions for use in [this article]().

## Connect the host and the Pico

First, connect the host to the Pico using a USB **data** lead. Some USB leads only supply power. They will not work.

## Install software on the Pico

Next, install the `blinker` script.

The `blinker.py` runs on the Pico.

1. Install it on the Pico using the `Thonny` editor.
    1. Open the gist on GitHib.
    1. Copy the code th your clipboard.
    1. Open `Thonny` and make sure it has connected to the Pico.
    1. Paste the code into the `Thonny` editor window.
    1. Save it on the Pico as `main.py`.
    1. Close the Thonny editor. 
   
*If you leave the Thonny editor open it will keep the serial port open on the host, and
the serial program will not work!*

Since you saved the program as `main.py` it will run on the Pico automatically.

The `sender.py` script runs on the host.
It uses PySerial to send commands from the host to the Raspberry Pi Pico and 
read the result.

To use it, *on the host*

1. Run `pip3 install pyserial`.
1. Copy `sender.py` into a directory of your choice.
1. In that directory, run `python3` to start an interactive session.
1. Type `from sended import Sender`
1. Type `s = Sender()`. If you are running on Windows, you will need to type 
   `s = Sender('COM6')` replacing `COM6` by whatever port the Pico is visible on.   
1. Type `s.send('2 + 2')`
1. Type `s.receive()`. If all is well, this will print the result 4.
1. Type `s.send('on()'`. The on-board LED on the Pico should turn on.
1. Type `s.send('off()'`. The on-board LED on the Pico should turn off.
1. When you have finished, type `s.close()`.




