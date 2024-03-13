from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Helps reduce code'

# Setting up
setup(
    name="finder-vsv170314",
    version=VERSION,
    author="VSV170314 (Vishwa S Vikram)",
    author_email="<mail@vishwa170314.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'code', 'reduce', 'code reduce', "work_less", "less_code", "clean_code"],
    classifiers=[
        "Development Status :: 1 - releasing",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
