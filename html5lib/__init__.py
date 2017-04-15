"""
HTML parsing library based on the WHATWG "HTML5"
specification. The parser is designed to be compatible with existing
HTML found in the wild and implements well-defined error recovery that
is largely compatible with modern desktop web browsers.

Example usage::

    import html5lib
    with open("my_document.html", "rb") as f:
        tree = html5lib.parse(f)

For convenience, this module re-exports the following names:

* :func:`~.html5parser.parse`, :func:`~.html5parser.parseFragment`, and :class:`~.html5parser.HTMLParser`
* :func:`~.treebuilders.getTreeBuilder`
* :func:`~.treewalkers.getTreeWalker`
* :func:`~.serializer.serialize`
"""

from __future__ import absolute_import, division, unicode_literals

from .html5parser import HTMLParser, parse, parseFragment
from .treebuilders import getTreeBuilder
from .treewalkers import getTreeWalker
from .serializer import serialize

__all__ = ["HTMLParser", "parse", "parseFragment", "getTreeBuilder",
           "getTreeWalker", "serialize", "__version__"]

# this has to be at the top level, see how setup.py parses this
#: Distribution version number, which asymptotically approaches 1.
__version__ = "0.9999999999-dev"
