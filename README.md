# Code for *Raspberry Pi Pico*

Some projects also requires an attached Raspberry Pi (the *host*) running additional code.

The `docs/<project>.md` file describes each project.

Code for the Pico is in `src/pico_code/pico`.
Code for the Host is in `src/pico_code/host`.

Host code has been tested on a Raspberry Pi connected to a Raspberry Pi Pico under Python 3.7. It may need modification to run on other Linux, Windows or Mac computers.

## Talker 

The [first project](docs/talker.md) `talker` uses  a Talker bused on PySerial to send commands from the Pi to the Pico and read  output from the Pi.


## Function Generator

[fungen](docs/fungen.md) is a minimalist AF (Audio Frequency) generator based on the Pico.

## MCO3008

[mcp3008](mcp3008.md) is a MicroPython driver for the MCP3008 80-channel SPI ADC.

## (Very) Experimental VS Code support

I have started exploring VS Code. If you look in the `.vscode` directory you'll see a `tasks.json` file that sets up user tasks.They invoke scripts that use ampy to copy a file or the contents of a directory, and one (*use with care!*) that will remove *all* the .py files from the Pico.

1. `pico list` lists all the files on the pico.
1. `pico put all` requires you to have a file open in the editor. It copies *all* the files in the parent directory from the host to the pico.
1. `pico put` copies the currently open file from the host to the pico.
1. `pico clear` asks for confirmation, and then removes all files from the pico. **Use it with care!**.

The scripts (which are in the `scripts` directory) are currently Linux-only; I have tested them with Linux Mint on a workstation and with Raspberry Pi OS on a Pi.

I'd be delighted if someone with access to Windows or Mac OSX could add scripts annd edit the `tasks.json` file to make the tasks available in those enviroments.

You'll need to use `chmod` to make the scripts executable, and you need to install `ampy`.

```
cd scripts
chmod a+x *.sh
sudo python3 -m pip install adafruit-ampy
```


