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


