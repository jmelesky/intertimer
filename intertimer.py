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

    main([{'length': 5, 'message': 'interval 1'}, {'length': 2, 'message': 'interval 2'}], 3)
