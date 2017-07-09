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

How it works
------------

pykeepachangelog is a wrapper on top of [misaka][] Markdown parser. It
expects a file that follows the format specified by [Keep a Changelog][]
and returns the information described in a structured way (per version
and section).

Contributing
------------

Pull requests are welcomed. Before submiting you code for review, please make
sure all the tests passed after your change:

.. code-block:: bash

   $ pytest


License
-------

This project is licensed under [MIT license][license]. For details please see
`LICENSE` file.


.. keepachangelog: https://keepachangelog.com
.. license: https://choosealicense.com/licenses/mit/
.. misaka: https://github.com/FSX/misaka
