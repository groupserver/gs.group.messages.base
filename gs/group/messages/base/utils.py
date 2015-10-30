# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright © 2013, 2014, 2015 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
from __future__ import unicode_literals, absolute_import, division, print_function
from math import pow, floor, log

#: The lookup table for the characters that represent the file-icons. The *type*
#: is used. For speed a slice used to check the first five characters. This
#: works well, for everything other than "text". If there is a miss then "other"
#: is used.
ICON_CHAR = {
    'image': unichr(127912),
    'audio': unichr(128265),
    'video': unichr(127910),
    'text/': unichr(128461),
    'other': unichr(128461), }


def get_icon(mimeType):
    '''Get the icon (character) for a particular MIME-type

:param str mimeType: The mime-type to look up
:returns: The character for the icon representing the MIME type
:rtype: unichr'''
    retval = ICON_CHAR.get(mimeType[:5], ICON_CHAR['other'])
    return retval


def file_size_format(bytes):
    """A humanized string for a given amount of bytes

:param int bytes: The number of bytes
:returns: The file size with the units
:rtype: str

.. seealso::

    The original version of this function <http://python.todaysummary.com/q_python_11123.html>"""
    bytes = int(bytes)
    if bytes is 0:
        retval = 'empty'
    else:
        l = floor(log(bytes, 1024))
        size = bytes / pow(1024, l)
        unit = [' bytes', 'kb', 'mb', 'gb', 'tb', 'pb', 'eb', 'zb', 'yb'][int(l)]
        sf = 2 if l > 0 else 0
        retval = '{size:.{sf}f}{unit}'.format(size=size, sf=sf, unit=unit)
    return retval
