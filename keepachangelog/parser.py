from misaka import Markdown

from keepachangelog.renderer import Renderer


def parse(text):
    chg = Renderer()
    chg.reset()

    md = Markdown(renderer=chg)
    md(text)
    return chg


def parse_file(fd):
    return parse(fd.read())
