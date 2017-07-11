pykeepachangelog
================

Parses changelogs that follows keepachangelog_ format, exposing the
data in a structured way.

Installation
------------

pykeepachangelog supports Python 2.7, 3.5 and 3.6.

.. code-block:: bash

   $ pip install pykeepachangelog

Usage
-----

.. code-block:: python

   import keepachangelog

   with open("CHANGELOG.md", "r") as fd:
       keepachangelog.parse_file(fd)

How it works
------------

pykeepachangelog is a wrapper on top of misaka_ Markdown parser. It
expects a file that follows the format specified by
`Keep a Changelog <keepachangelog_>`_ and returns the information
described in a structured way (per version and section).

Contributing
------------

Pull requests are welcomed. Before submiting you code for review,
please make sure all the tests passed after your change:

.. code-block:: bash

   $ pytest


License
-------

This project is licensed under `MIT license`_. For details please see
`LICENSE` file.


.. _keepachangelog: https://keepachangelog.com
.. _license: https://choosealicense.com/licenses/mit/
.. _misaka: https://github.com/FSX/misaka
