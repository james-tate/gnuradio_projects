#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Dec 28 16:39:00 2016
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

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2600000
        self.rf_tx = rf_tx = 0
        self.noise_amp = noise_amp = 0
        self.noise = noise = 0
        self.if_tx = if_tx = 30
        self.freq = freq = 1575420000

        ##################################################
        # Blocks
        ##################################################
        _rf_tx_sizer = wx.BoxSizer(wx.VERTICAL)
        self._rf_tx_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_rf_tx_sizer,
        	value=self.rf_tx,
        	callback=self.set_rf_tx,
        	label='RF_AMP',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._rf_tx_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_rf_tx_sizer,
        	value=self.rf_tx,
        	callback=self.set_rf_tx,
        	minimum=0,
        	maximum=14,
        	num_steps=14,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_rf_tx_sizer)
        _if_tx_sizer = wx.BoxSizer(wx.VERTICAL)
        self._if_tx_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_if_tx_sizer,
        	value=self.if_tx,
        	callback=self.set_if_tx,
        	label='IF_AMP',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._if_tx_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_if_tx_sizer,
        	value=self.if_tx,
        	callback=self.set_if_tx,
        	minimum=0,
        	maximum=47,
        	num_steps=47,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_if_tx_sizer)
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + "serial=F4C33C" )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(freq, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(rf_tx, 0)
        self.osmosdr_sink_0.set_if_gain(if_tx, 0)
        self.osmosdr_sink_0.set_bb_gain(20, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(2.5e6, 0)

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
        	maximum=10,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_noise_amp_sizer)
        self._noise_check_box = forms.check_box(
        	parent=self.GetWin(),
        	value=self.noise,
        	callback=self.set_noise,
        	label='noise',
        	true=1,
        	false=0,
        )
        self.Add(self._noise_check_box)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_short*1, '/home/james/Downloads/circle_hackrf.bin', True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.blocks_short_to_float_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_float_to_complex_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)

    def get_rf_tx(self):
        return self.rf_tx

    def set_rf_tx(self, rf_tx):
        self.rf_tx = rf_tx
        self._rf_tx_slider.set_value(self.rf_tx)
        self._rf_tx_text_box.set_value(self.rf_tx)
        self.osmosdr_sink_0.set_gain(self.rf_tx, 0)

    def get_noise_amp(self):
        return self.noise_amp

    def set_noise_amp(self, noise_amp):
        self.noise_amp = noise_amp
        self._noise_amp_slider.set_value(self.noise_amp)
        self._noise_amp_text_box.set_value(self.noise_amp)

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        self._noise_check_box.set_value(self.noise)

    def get_if_tx(self):
        return self.if_tx

    def set_if_tx(self, if_tx):
        self.if_tx = if_tx
        self._if_tx_slider.set_value(self.if_tx)
        self._if_tx_text_box.set_value(self.if_tx)
        self.osmosdr_sink_0.set_if_gain(self.if_tx, 0)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.osmosdr_sink_0.set_center_freq(self.freq, 0)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
