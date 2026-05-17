#!/usr/bin/env python3
from gnuradio import gr
from gnuradio import zeromq
import osmosdr
import signal
import sys


class top_block(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self)
        samp_rate = 500000
        self.src = osmosdr.source(args="numchan=1")
        self.src.set_sample_rate(samp_rate)
        self.src.set_center_freq(433.92e6)
        self.src.set_gain(25)
        self.pub = zeromq.pub_sink(
            gr.sizeof_gr_complex,
            1,
            "tcp://0.0.0.0:5000",
            100,
            False,
            -1
        )
        self.connect(self.src, self.pub)


tb = top_block()


def shutdown(sig=None, frame=None):
    tb.stop()
    tb.wait()
    sys.exit(0)


signal.signal(signal.SIGINT, shutdown)
signal.signal(signal.SIGTERM, shutdown)
tb.start()
signal.pause()
