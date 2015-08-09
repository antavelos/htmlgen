# -*- coding: utf-8 -*-
import cgi

from config import ALLOWED_TAGS

class Element(object):

    def __init__(self, tag, klass=None, eid=None, attrs=None, escape=True):
        assert type(tag) == str, "tag should be a string"
        assert tag in ALLOWED_TAGS, "Invalid tag: %s" % tag
        if attrs:
            assert type(attrs) == dict, "attrs should be a disctionary"
        self.tag = tag
        self.attrs = attrs if attrs else {}
        if klass:
            self.attrs['class'] = klass
        if eid:
            self.attrs['id'] = eid
        self.escape = escape
        self.text = ""
        self._subelements = []


    def get_inner(self):
        return "\n".join([str(el) for el in self._subelements])

    def append(self, element):
        assert type(element) == Element, "element should be a BaseElement"
        self._subelements.append(element)

        return self

    def _get_attrs(self):
        return " ".join(['%s="%s"' % (attr, value) \
                         for (attr, value) in self.attrs.items()])
    def _get_html(self):
        return "<%s %s>\n%s</%s>" % (self.tag, self._get_attrs(), \
                                     self.get_inner(), self.tag)

    def __str__(self):
        return cgi.escape(self._get_html()) if self.escape else self._get_html()
