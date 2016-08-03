#!/usr/bin/python3
#
# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 et sts=4 ai:


class ChannelInterface(object):
    def shutdown(self):
        """Cleanly shutdown the channel.
        
        """
        pass

    def terminate(self):
        pass


class PipelineInterface(object):
    def connect(self, **kw):
        """
        connect({"pad_a": channel_a, "pad_b": channel_b, "pad_c":None})
        connect({"pad_a": None, "pad_b": None, "pad_c": None})
        """
        pass

    def shutdown(self):
        pass

    def terminate(self):
        pass

    def replace(self, string):
        pass


    def update_properties(self, properties):
        """

        """
        pass


class PipelineManagerInterface(object):

    def create_channel(self, name):
        """Create a channel which connects pipelines.

        Raises an error if a channel with this name **already** exists.
        """
        pass

    def create_file_channel(self, name, fd):
        """Transfer a file descriptor object to the pipeline manager.

        The function will return an opaque reference which can now be used as a
        sink or source in pipelines.

        .. warning::
           
           It is important that program no longer access the file descriptor
           after passing it to the manager!

        :param fd: An object with fileno() method returning a "file descriptor".
        :rtype: Return a channel object which can be connected to pipelines.
        """
        pass

    def get_channel(self, name):
        """Get an already existing channel in the manager.
        
        Raises an error if a channel with this name **doesn't** exist.
        """
        pass

    def create_pipeline(self, name, pipeline, input_pads={}, output_pads={}):
        """Create a new gstreamer pipeline in the manager.

        :param pipeline: A string containing a gstreamer pipeline that can be
                         passed to gst_parse_string.
        :rtype: An opaque reference to the new pipeline which can be used to
                control the pipeline.

        Raises an error if the creation failed.
        """
        pass

    def get_pipeline(self, name):
        """Get an existing pipeline in the manager.

        Raises an error if a channel with this name **doesn't** exist.
        """
        pass

