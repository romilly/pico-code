# Testing a Pico-based function generator

## Wed 3 Feb 2021

I've been working on a minimalist digital Oscillosocope based on a Raspeebrry Pi Pico
and I need a way of generating AF (audio frequency) waveforms to test it with.

Yesterday I set up a very simple *function generator* which (I hope) produces a sine wave output.
It uses the Pico's PIO capability and it's based on a hacked version of one of the PIO MicorPython demos.

I have a Bitscope micro USB-based oscilloscope which I am going to use to test the function generator.

I'll update this gist as I go, and will publish the code here once I know it's working.

Aand it works! Code below.

### Next step

I will add a couple of potentiometers so I can vary frequency and amplitude.

### Time for a pause.

Reading analogue signals has strange effects, and I think I may need to use `_thread`.

More soon.

## Friday 5 Feb 2021

I have a potentiometer controlling frequency running in a thread. It works fiune upto about 2 kHz.
This has been fun, hence the name :) but I really need a wider range of frequencies to test the Pi Pico 'Scope code.

I've ordered an external ADC and will see if that will give me what I want..

