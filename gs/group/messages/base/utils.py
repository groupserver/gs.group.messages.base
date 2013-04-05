# -*- coding: utf-8 -*-
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
