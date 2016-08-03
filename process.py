#!/usr/bin/python3
import logging
from gi.repository import Gst




mixerpad.get_by_name('mix').get_static_pad('sink_%u' % idx)
mixerpad.set_property('volume', volume)

"""
			interaudiosrc channel=audio_{channel} !
			{acaps} !
			queue !
			mux.
			intervideosrc channel=video_{channel} !
			{vcaps_in} !
"""


fdsink.emit('add', conn.fileno())
fdsink.connect('client-fd-removed', on_disconnect)


gst_pipeline = Gst.parse_launch(pipeline)
gst_pipeline.bus.add_signal_watch()
gst_pipeline.bus.connect("message::eos", self.on_eos)
gst_pipeline.bus.connect("message::error", self.on_error)
gst_pipeline.set_state(Gst.State.PLAYING)
gst_pipeline.set_state(Gst.State.NULL)


capsfilter = gst_pipeline.get_by_name('caps_%u' % idx)
capsfilter.set_property('caps', caps)
