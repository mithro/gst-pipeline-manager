Start of an idea around a "gstreamer pipeline manager". Not actually anything
which works.

The idea is that you have x gstreamer pipelines connected by "gaps" (like the
inter elements or gdppay/gdpdepay elements) and you want to be able to
update/change them in real time without disrupting the flow of data.

If a change fails to apply, it should be able to be rolled back, etc.

Based on ideas from;
 * flumotion
 * gst-switch
 * voctomix


