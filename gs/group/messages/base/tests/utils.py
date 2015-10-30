# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2015 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from __future__ import absolute_import, unicode_literals
from unittest import TestCase
from gs.group.messages.base.utils import (file_size_format, get_icon, ICON_CHAR)


class TestFileSizeFormat(TestCase):
    '''Tests for the ``file_size_format`` utility'''

    def test_file_size_empty(self):
        r = file_size_format(0)
        self.assertEqual('empty', r)

    def test_file_size_bytes(self):
        r = file_size_format(10)
        self.assertEqual('10 bytes', r)

    def test_file_size_kb(self):
        r = file_size_format(2047)
        self.assertEqual('2.00kb', r)

    def test_file_size_mb(self):
        r = file_size_format(2047*1000)
        self.assertEqual('1.95mb', r)

    def test_file_size_gb(self):
        r = file_size_format(2047*1000*1000)
        self.assertEqual('1.91gb', r)

    def test_file_size_tb(self):
        r = file_size_format(2047*1000*1000*1000)
        self.assertEqual('1.86tb', r)


class TestGetIcon(TestCase):
    ''''Tests the ``get_icon`` utility'''

    def assertIcon(self, name, value):
        self.assertEqual(ICON_CHAR[name], value, 'Expected a {0} icon'.format(name))

    def test_other(self):
        m = 'application/x-groupserver-test'
        r = get_icon(m)
        self.assertIcon('other', r)

    def test_img_png(self):
        m = 'image/png'
        r = get_icon(m)
        self.assertIcon('image', r)

    def test_img_jpeg(self):
        m = 'image/jpeg'
        r = get_icon(m)
        self.assertIcon('image', r)

    def test_img_jpg(self):
        m = 'image/jpg'
        r = get_icon(m)
        self.assertIcon('image', r)

    def test_plain(self):
        m = 'text/plain'
        r = get_icon(m)
        self.assertIcon('text/', r)

    def test_html(self):
        m = 'text/html'
        r = get_icon(m)
        self.assertIcon('text/', r)

    def test_audio(self):
        m = 'audio/ogg'
        r = get_icon(m)
        self.assertIcon('audio', r)

    def test_video(self):
        m = 'video/webm'
        r = get_icon(m)
        self.assertIcon('video', r)
