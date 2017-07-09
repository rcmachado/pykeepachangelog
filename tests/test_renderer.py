from datetime import date

import pytest

from keepachangelog.renderer import ChangelogParserMixin, parse_version


class TestChangelogParserMixin:
    def test_reset_should_redefine_internal_state(self):
        chg = ChangelogParserMixin()
        chg.versions = {'dummy': 'something'}
        chg._current_version = 'dummy'
        chg._current_section = 'something'

        chg.reset()

        assert not chg.versions
        assert chg._current_version is None
        assert chg._current_section is None

    def test_header_with_version_and_release(self):
        chg = ChangelogParserMixin()
        chg.reset()

        chg.header("[v1.2.3] - 2017-07-01", level=2)
        assert "v1.2.3" in chg.versions
        assert chg.versions["v1.2.3"]["release_date"] == date(2017, 7, 1)
        assert not chg.versions["v1.2.3"]["sections"]

    def test_header_with_section(self):
        chg = ChangelogParserMixin()
        chg.reset()

        chg.header("[v1.2.3] - 2017-07-01", level=2)
        chg.header("Added", level=3)
        assert "Added" in chg.versions["v1.2.3"]["sections"]

    def test_listitem_with_entry(self):
        chg = ChangelogParserMixin()
        chg.reset()

        chg.header("[v1.2.3] - 2017-07-01", level=2)
        chg.header("Fixed", level=3)
        chg.listitem("Bug with add an item feature", False, False)

        entries = chg.versions["v1.2.3"]["sections"]["Fixed"]
        assert "Bug with add an item feature" in entries

    def test_changelog_for_specific_version(self):
        chg = ChangelogParserMixin()
        chg.reset()
        chg.header("[v1.2.3] - 2017-07-01", level=2)
        chg.header("Added", level=3)
        chg.listitem("Feature to add an item", False, False)
        chg.header("Fixed", level=3)
        chg.listitem("Bug with add an item feature", False, False)

        expected = """## Added
- Feature to add an item

## Fixed
- Bug with add an item feature"""

        changelog_text = chg.changelog_for("v1.2.3")
        assert expected == changelog_text

    def test_changelog_for_unknown_version_raises_error(self):
        chg = ChangelogParserMixin()
        with pytest.raises(ValueError):
            chg.changelog_for("v1.2.3")


@pytest.mark.parametrize("version_str,version,release_date", [
    ("[1.2.3] - 2017-07-01", "1.2.3", date(2017, 7, 1)),
    ("[v4.5.6] - 2017-07-02", "v4.5.6", date(2017, 7, 2)),
    ("[Unreleased]", "Unreleased", None),
    ("7.8.9 - 2017-07-03", "7.8.9", date(2017, 7, 3)),
])
def test_parse_version(version_str, version, release_date):
    result = parse_version(version_str)
    assert version == result["version"]
    assert release_date == result["release_date"]
