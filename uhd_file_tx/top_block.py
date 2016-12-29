#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Dec 28 22:33:07 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2500000
        self.noise_amp = noise_amp = 0
        self.freq = freq = 1575420000

        ##################################################
        # Blocks
        ##################################################
        _noise_amp_sizer = wx.BoxSizer(wx.VERTICAL)
        self._noise_amp_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_noise_amp_sizer,
        	value=self.noise_amp,
        	callback=self.set_noise_amp,
        	label='Noise',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._noise_amp_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_noise_amp_sizer,
        	value=self.noise_amp,
        	callback=self.set_noise_amp,
        	minimum=0,
        	maximum=5e3,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_noise_amp_sizer)
        self.uhd_usrp_sink = uhd.usrp_sink(
        	",".join(("serial=F4C33C", "master_clock_rate=50e6")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink.set_subdev_spec('A:A', 0)
        self.uhd_usrp_sink.set_samp_rate(samp_rate)
        self.uhd_usrp_sink.set_center_freq(freq, 0)
        self.uhd_usrp_sink.set_gain(80, 0)
        self.uhd_usrp_sink.set_antenna('TX/RX', 0)
        self.blocks_interleaved_short_to_complex_0 = blocks.interleaved_short_to_complex(False, False)
        self.blocks_file_source = blocks.file_source(gr.sizeof_short*1, '/home/james/Desktop/gps-sdr-sim/gpssim.bin', True)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_UNIFORM, noise_amp , 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.uhd_usrp_sink, 0))
        self.connect((self.blocks_file_source, 0), (self.blocks_interleaved_short_to_complex_0, 0))
        self.connect((self.blocks_interleaved_short_to_complex_0, 0), (self.blocks_add_xx_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_sink.set_samp_rate(self.samp_rate)

    def get_noise_amp(self):
        return self.noise_amp

    def set_noise_amp(self, noise_amp):
        self.noise_amp = noise_amp
        self._noise_amp_slider.set_value(self.noise_amp)
        self._noise_amp_text_box.set_value(self.noise_amp)
        self.analog_noise_source_x_0.set_amplitude(self.noise_amp )

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.uhd_usrp_sink.set_center_freq(self.freq, 0)
        self.uhd_usrp_sink.set_center_freq(self.freq, 1)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
