====================================
Hierarchical and temporal navigation
====================================

:Authors: `Michael JasonSmith`_; `Dan Randow`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2015-10-16
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 4.0 International License`_
  by `OnlineGroups.Net`_.

.. _Creative Commons Attribution-Share Alike 4.0 International License:
    http://creativecommons.org/licenses/by-sa/4.0/

Hierarchy
=========

There is a hierarchy of pages in GroupServer. The **primary**
hierarchy is (from most general to most specific) Site, Group,
Topic, Post, Image. This hierarchy is shown in the *breadcrumbs*
going from left to right. Conceptually the site is at the top and
any **up** link goes up to the page that is higher in the
hierarchy, so there is a slightly awkward mapping of *Left* in
the breadcrumbs onto *Up* in the navigation links.

It is possible that in future versions of GroupServer that this
mapping may be removed, so the *Left* navigation button (or
swiping to the right) will go the containing (more general) page.

Temporal navigation
===================

The temporal navigation of messages in a group may seem
inconsistent. However, it follows the principal of supporting the
user's task: `follow closely`_, or `keep in the loop`_. We switch
mode because the user is switching mode; this is in tension with
consistency.

Follow closely
--------------

If the user is following something closely then the posts are
shown in a strict temporal order with the oldest post first. This
is similar to a book, or a diary. There is **one page** that
follows this order: `the Topic page`_. This makes reading the
conversation much easier.

Two other pages take their queue from the Topic page for
organising the **navigation links**.

* **The Post page** has four links: First, Older, Up, Newer,
  Last. 
* **The Image page** has three links: Older, Up, Newer. The *Up*
  link goes to the post.

Because *Up* has been taken for the page hierarchy_, *Left* has
been mapped to *Up* in the sense of moving higher on the *Topic*
page.

.. _the Topic page:
   https://github.com/groupserver/gs.group.messages.topic.base

Keep in the loop
----------------

*Keeping in the loop* is the other task supported by
GroupServer. For interfaces that support this task the posts (or
topics) are displayed from newest to oldest. These pages include:

* The *Site* page, which lists topics
* The *Group* page that lists topics, post, and files
* The rarely visited *Topics* page
* The even more rarely visited *Posts* page

In all these pages the *Left* navigation button has been mapped
to *Up* in the sense of moving higher on in the list. So as all
these interfaces show posts from newest to oldest *Left* is the
same as *Newer*.

..  _GroupServer: http://groupserver.org/
..  _GroupServer.org: http://groupserver.org/
..  _OnlineGroups.Net: https://onlinegroups.net/
..  _Michael JasonSmith: http://groupserver.org/p/mpj17
..  _Dan Randow: http://groupserver.org/p/danr
..  _Bill Bushey: http://groupserver.org/p/wbushey
..  _Alice Rose: https://twitter.com/heldinz
..  _E-Democracy.org: http://forums.e-democracy.org/
