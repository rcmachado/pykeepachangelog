pykeepachangelog
================

Parses changelogs that follows [keepachangelog][] format, exposing the data in
a structured way.

Installation
------------

.. code-block:: bash

   $ pip install pykeepachangelog

Usage
-----

.. code-block:: python

   import keepachangelog

   with open("CHANGELOG.md", "r") as fd:
       keepachangelog.parse_file(fd)

.. keepachangelog: https://keepachangelog.com
