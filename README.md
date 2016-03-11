# intertimer

A simple command-line interval timer, written in python3

    usage: intertimer.py [-h] [-i INTERVAL] [-n NAME] [-c LOOPS]
    
    optional arguments:
      -h, --help            show this help message and exit
      -i INTERVAL, --interval INTERVAL
      -n NAME, --name NAME
      -c LOOPS, --loops LOOPS


### Usage

intertimer can handle any number of different intervals, looped any number of times.

Pomodoro timings:

    ./intertimer.py -i 1500 -n Pomodoro -i 300 -n "Short break!" -c 4

10/20/30 intervals, fifteen times:

    ./intertimer.py -i 10 -n slow -i 20 -n medium -i 30 -n "fast!" -c 15


### Notes

intertimer uses the ASCII 'beep' character (ASCII 7), printed to the
terminal, to help signal the change in interval. Some terminals
(notably the Windows command prompt) don't "display" the beep
correctly, or end up configured not to play any beep at all. YMMV.

