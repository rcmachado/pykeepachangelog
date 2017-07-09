from keepachangelog.parser import parse, parse_file


def test_parse(standard_changelog):
    chg = parse(standard_changelog)
    data = chg.versions["1.0.0"]
    assert len(data["sections"]["Changed"]) == 13
    assert data["sections"]["Added"][1] == "Version navigation."


def test_parse_file(fileobj_changelog):
    chg = parse_file(fileobj_changelog)
    data = chg.versions["1.0.0"]
    assert len(data["sections"]["Changed"]) == 13
    assert data["sections"]["Added"][1] == "Version navigation."
