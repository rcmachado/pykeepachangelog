from __future__ import absolute_import, unicode_literals

import re
from collections import OrderedDict
from datetime import datetime

from misaka import BaseRenderer


class ChangelogParserMixin(object):
    versions = None
    _current_version = None
    _current_section = None

    def reset(self):
        self.versions = {}
        self._current_version = None
        self._current_section = None

    def header(self, content, level):
        if level == 2:
            data = parse_version(content)
            v = data["version"]
            self.versions[v] = {
                "release_date": data["release_date"],
                "sections": OrderedDict(),
            }
            self._current_version = v
            self._current_section = None
        elif level == 3:
            self.versions[self._current_version]["sections"][content] = []
            self._current_section = content

    def listitem(self, content, is_ordered, is_block):
        self.versions[self._current_version]["sections"][self._current_section].append(content.strip())

    def changelog_for(self, version):
        if not self.versions or version not in self.versions:
            raise ValueError("Unknown version {}".format(version))

        content = ""
        for section, items in self.versions[version]["sections"].items():
            content += "## {section}\n".format(section=section)
            for item in items:
                content += "- {item}\n".format(item=item.replace("\n", " "))
            content += "\n"
        return content.strip()


class Renderer(ChangelogParserMixin, BaseRenderer):
    pass


def parse_version(title):
    m = re.match(r"\[?(?P<version>[^(\]|\s)]+)\]? - (?P<release_date>\d{4}-\d{2}-\d{2})$", title)
    if m:
        return {
            "version": m.group("version"),
            "release_date": (datetime.strptime(m.group("release_date"),
                                               "%Y-%m-%d")
                             .date()),
        }

    m = re.match(r"\[(?P<version>Unreleased)\]$", title)
    if m:
        return {
            "version": m.group("version"),
            "release_date": None,
        }
