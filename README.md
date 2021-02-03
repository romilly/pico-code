# Code for *Raspberry Pi Pico*

Some projects also requires an attached Raspberry Pi (the *host*) running additional code.

The `src/<project>/README.md` file describes each project.

The `src/<project>pico` folder contains code the relevant project for the Pico.

If present, code in the `src/<project>/host` folder has been tested on a Raspberry Pi connected to a 
Raspberry Pi Pico under Python 3.7. It may need modification to run on other Linux, Windows or Mac computers.

## Talker 

The [first project](src/talker/README.md) `talker` uses  a Talker bused on PySerial to send commands from the Pi to the
Pico and read  output from the Pi.


## Function Generator

[fungen](src/fungen/README.md) is a minimalist AF (Audio Frequency) generator based on the Pico.


