#!/usr/bin/python3

import time
import struct

with open("/dev/ldusb0", 'rb') as ldusb:
    time.sleep(0.5)

    # for n in range(10):
    while True:
        # time.sleep(0.5)
        pkt = ldusb.read(8)
        parsed_pkt = list(struct.unpack("<BBHHH", pkt))
        num_samples = parsed_pkt.pop(0)
        seqno = parsed_pkt.pop(0)
        for sample in range(num_samples):
            print(seqno+sample, parsed_pkt[sample]/128.0)
        # time.sleep(0.5)

# vim: set sw=4 ts=4 et:
