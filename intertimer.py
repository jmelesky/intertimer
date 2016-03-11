#!/usr/bin/env python3

import time

def main(intervals, loopcount):
    for i in (range(0, loopcount)):
        for interval in intervals:
            msg = interval['message']
            dur = interval['length']
            print(chr(7) + msg)
            time.sleep(dur)
    print("done!" + chr(7))



if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--interval', action='append')
    parser.add_argument('-n', '--name', action='append')
    parser.add_argument('-c', '--loops', default='5', type=int)

    args = parser.parse_args()

    lengths = []
    if args.interval:
        lengths = args.interval

    names = []
    if args.name:
        names = args.name

    intervals = []
    for i in range(0, len(lengths)):
        name = 'Interval %s' % (i + 1)
        if len(names) > i:
            name = names[i]
        intervals += [{'length': int(lengths[i]),
                       'message': name}]

    main(intervals, args.loops)

