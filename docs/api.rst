=================================
:mod:`gs.group.messages.base` API
=================================

.. currentmodule:: gs.group.messages.base

There are two parts to the API supplied by the
:mod:`gs.group.messages.base` product: there is a viewlet_ and
some utilities_.

Viewlet
=======

The :mod:`gs.group.messages.base` product supplies a *viewlet* —
for the group page (:mod:`gs.group.home`) — called
``gs-group-messages-base``. In turn it contains a *viewlet
manager* that creates a slot for the various views of the list of
messages. (In the user-documentation this is generally referred
to as *the archive*.)

The viewlet manager provides the interface
:class:`.interfaces.IGroupHomepageMessages`.

.. autoclass:: gs.group.messages.base.interfaces.IGroupHomepageMessages

The viewlets that provide lists for the *Group* page register
against this interface.

.. code-block:: xml

  <browser:viewlet 
    name="gs-group-messages-topics-tab"
    manager="gs.group.messages.base.interfaces.IGroupHomepageMessages"
    template="browser/templates/topics.pt"
    class=".topicstab.TopicsTab"
    permission="zope2.Public"
    weight="10"
    title="Topics" />

The viewlets and viewlet manager combine to create tabs, using
the `Bootstrap tabs`_ system. The ``title`` of each viewlet
becomes the tab-title, with the content of the viewlet becoming
the tab-panel. All the tabs are marked-up with `WAI:ARIA
roles`_. The viewlet itself has the HTML ``id`` attribute value
``gs-group-messages-base-tabs``

Utilities
=========

There are utilities for `file icons`_ and for formatting `file
sizes`_. These happen to be used in many different contexts, so
the functions are placed here.

File icons
----------

In GroupServer the file icons are actually characters. The icon
font supplied by :mod:`gs.content.css` turns the character into a
glyph.

.. autofunction:: gs.group.messages.base.get_icon

Example
~~~~~~~

 Call the function::
            
   f['icon'] = get_icon(f['mime_type'])

 Use the icon in the page template:

 .. code-block:: xml

    <a class="icon-alone" href="#" tal:attributes="href f/url; title f/name">
      <span aria-hidden="true" data-icon="&#x1f3a8;"
            tal:attributes="data-icon f/icon"></span>
      <span class="screen-reader-text">File type:
        <span tal:content="f/mime_type">application/octet-stream</span>
      </span>
    </a>

File sizes
----------

File sizes are displayed in the list of attached posts in both
email and on the web, and on the *Image* page, hence the presence
of the :func:`file_size_format` function here. It formats the
size so it has the appropriate unit (b, kb, mb, gb, tb…) after
it, or it displays ``empty``.

.. autofunction:: gs.group.messages.base.file_size_format

.. [#groupPage] The main section of the Group page is provided by
                ``gs.group.home.interfaces.IGroupHomepageMain``. See
                ``gs.group.home``
                <https://github.com/groupserver/gs.group.home>
.. _viewlet manager: http://docs.zope.org/zope.viewlet/index.html
.. _Bootstrap tabs: http://getbootstrap.com/2.3.2/javascript.html#tabs
.. _WAI:ARIA roles: http://www.w3.org/TR/wai-aria/roles

..  LocalWords:  viewlets
