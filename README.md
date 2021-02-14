# Code for *Raspberry Pi Pico*

Some projects also requires an attached Raspberry Pi (the *host*) running additional code.

The `docs/<project>.md` file describes each project.

Code for the Pico is in `src/pico_code/pico`.

code for the Host is in `src/pico_code/host`. Host code has been tested on a Raspberry Pi connected to a 
Raspberry Pi Pico under Python 3.7. It may need modification to run on other Linux, Windows or Mac computers.

## Talker 

The [first project](docs/talker.md) `talker` uses  a Talker bused on PySerial to send commands from the Pi to the
Pico and read  output from the Pi.


## Function Generator

[fungen](docs/fungen.md) is a minimalist AF (Audio Frequency) generator based on the Pico.

## MCO3008

[mcp3008](mcp3008.md) is a MicroPython driver for the MCP3008 80-channel SPI ADC.

## (Very) Experimental vs code support

I have started exploring VS Code. If you look in the .vscode directory you'll see a tasks.jsopn file that sets up user tasks. They invoke scripts that use ampy to copy a file or the contents of a directory, and one (use with are!) that will remove all the .py files from the Pico.

The scripts (in the scriots directory) are linux-only; I have tested them with Linux Mint on a workstation and with Raspberry Pi OS on a Pi.

You'll need to use chmod to make the scripts executable, and you need to install ampy.

```
cd scripts
chmod a+x *.sh
sudo python3 -m pip install adafruit-ampy
```


