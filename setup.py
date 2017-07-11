from codecs import open
from os import path
from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))


# Get the long description from the README file
with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="pykeepachangelog",
    description=("Parse and extract information from changelogs that follows "
                 "the keepachangelog.com format"),
    long_description=long_description,
    url="https://github.com/rcmachado/pykeepachangelog",
    author="Rodrigo Machado",
    author_email="rcmachado@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: ",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Build Tools",
    ],
    keywords="changelog keepachangelog",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "misaka",
    ],
    extras_require={
        "test": ["pytest", "tox"],
    },
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
)
