==========================
``gs.group.messages.base``
==========================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Core messages support for GroupServer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2015-03-04
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 4.0 International License`_
  by `OnlineGroups.Net`_.

.. _Creative Commons Attribution-Share Alike 4.0 International License:
    http://creativecommons.org/licenses/by-sa/4.0/


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
``gs.group.messages.base.interfaces.IGroupHomepageMessages`` interface:

.. code-block:: xml

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

Utilities
=========

There is one utility provided by this product: `get_icon`_.

``get_icon``
------------

Get the icon for the associated MIME-type.

:Synopsis: ``get_icon(mimeType)``

:Description: A message may have one or more files associated with
              it. Files can be represented by icons. These icons represent
              the *type* of file, as encoded by the MIME-type. The
              ``get_icon`` function maps MIME-types to icons.

:Arguments: ``mimeType``: The MIME-type of the file, as a string.

:Returns: A single Unicode character representing the icon for the
          file. The icons are supplied by the CSS product [#css]_.

:Example: Call the function::
            
            f['icon'] = get_icon(f['mime_type'])

          Use the icon in the page template:

          .. code-block:: xml

            <a class="icon-alone" href="#"
               tal:attributes="href f/url; title f/name">
               <span aria-hidden="true" data-icon="&#x1f3a8;"
                     tal:attributes="data-icon f/icon"></span>
               <span class="screen-reader-text">File type:
                 <span tal:content="f/mime_type">application/octet-stream</span>
               </span>
            </a>

Resources
=========

- Code repository: https://github.com/groupserver/gs.group.messages.base
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17

.. [#groupPage] The main section of the Group page is provided by
                ``gs.group.home.interfaces.IGroupHomepageMain``. See
                ``gs.group.home``
                <https://github.com/groupserver/gs.group.home>
.. _viewlet manager: http://docs.zope.org/zope.viewlet/index.html
.. [#others] See ``gs.group.messages.posts``
             <https://github.com/groupserver/gs.group.messages.posts/>,
             and ``gs.group.messages.topics``
             <https://github.com/groupserver/gs.group.messages.topics/>.
.. _Bootstrap tabs: http://twitter.github.com/bootstrap/javascript.html#tabs
.. _WAI:ARIA roles: http://www.w3.org/TR/wai-aria/roles
.. [#css] See ``gs.content.css``
             <https://github.com/groupserver/gs.content.css/>
