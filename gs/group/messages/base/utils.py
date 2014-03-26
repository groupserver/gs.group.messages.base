# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright © 2013, 2014 OnlineGroups.net and Contributors.
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
from __future__ import unicode_literals

# The lookup table for the characters that represent the file-icons. The *type*
# is used. For speed a slice used to check the first five characters. This
# works well, for everything other than "text". If there is a miss then "other"
# is used.
ICON_CHAR = {
        'image': unichr(127912),
        'audio': unichr(128265),
        'video': unichr(127910),
        'text/': unichr(128461),
        'other': unichr(128461),
    }


def get_icon(mimeType):
    retval = ICON_CHAR.get(mimeType[:5], ICON_CHAR['other'])
    return retval
