==========================
``gs.group.messages.base``
==========================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Core messages support for GroupServer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2013-03-21
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 3.0 New Zealand License`_
  by `OnlineGroups.Net`_.

Introduction
============

This is the core code for displaying messages in a `GroupServer`_
group. This module supplies two things:

* Some help (``gs-group-messages-help``), and
* A JavaScript viewlet_.

Viewlet
=======

The viewlet ``gs-group-messages-base-script`` appears on the main-section
of the Group page [#groupPage]_. It provides a `viewlet manager`_ that is
used by the different messages products that want to appear on the the
group page [#others]_. The manager provides the
``gs.group.messages.base.interfaces.IGroupHomepageMessages`` interface::

  <browser:viewlet 
    name="gs-group-messages-topics-tab"
    manager="gs.group.messages.base.interfaces.IGroupHomepageMessages"
    template="browser/templates/topics.pt"
    class=".topicstab.TopicsTab"
    permission="zope2.Public"
    weight="10"
    title="Topics" />

The viewlet and viewlet manager combine to create tabs, using the
`Bootstrap tabs`_ system. The ``title`` of each viewlet becomes the
tab-title, with the content of the viewlet becoming the tab-panel. All the
tabs are marked-up with `WAI:ARIA roles`_. The viewlet itself has the HTML
identifier ``gs-group-messages-base-tabs``.

Resources
=========

- Code repository: https://source.iopen.net/groupserver/gs.group.messages.base
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17
.. _Creative Commons Attribution-Share Alike 3.0 New Zealand License:
   http://creativecommons.org/licenses/by-sa/3.0/nz/

.. [#groupPage] The main section of the Group page is provided by
                ``gs.group.home.interfaces.IGroupHomepageMain``. See
                ``gs.group.home``
                <https://source.iopen.net/groupserver/gs.group.home>
.. _viewlet manager: http://docs.zope.org/zope.viewlet/index.html
.. [#others] See ``gs.group.messages.posts``
             <https://source.iopen.net/groupserver/gs.group.messages.posts>,
             and ``gs.group.messages.topics``
             <https://source.iopen.net/groupserver/gs.group.messages.topics>.
.. _Bootstrap tabs: http://twitter.github.com/bootstrap/javascript.html#tabs
.. _WAI:ARIA roles: http://www.w3.org/TR/wai-aria/roles
