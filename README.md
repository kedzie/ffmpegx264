ffmpeg-x264-python
==================

x264 two-pass encoding python script

* x264 executable will show usage information
* works on multiple files

Examples
--------
* Encode all VOB files into 2M bitrate X264 in MP4 container

    x264 *.VOB --bit_rate=2M --preset=faster --extension=mp4
* Use custom audio encoding

    x264 *.VOB -b 2M -p faster -x mp4 --audio="c:a libmp3lame -b:a 148KB"
