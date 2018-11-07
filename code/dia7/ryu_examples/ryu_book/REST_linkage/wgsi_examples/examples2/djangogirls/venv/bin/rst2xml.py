#!/home/tigarto/Documents/tesis_2018-2/sdn_repaso/code/dia7/ryu_examples/ryu_book/REST_linkage/wgsi_examples/examples2/djangogirls/venv/bin/python

# $Id: rst2xml.py 4564 2006-05-21 20:44:42Z wiemann $
# Author: David Goodger <goodger@python.org>
# Copyright: This module has been placed in the public domain.

"""
A minimal front end to the Docutils Publisher, producing Docutils XML.
"""

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline, default_description


description = ('Generates Docutils-native XML from standalone '
               'reStructuredText sources.  ' + default_description)

publish_cmdline(writer_name='xml', description=description)
