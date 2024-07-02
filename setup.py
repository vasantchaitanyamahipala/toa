from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Packages that allows you to communicate with llms and gets you back a audio file'

# Setting up
setup(
    name="audiobuddy",
    version=VERSION,
    author="VC (Vasant Chaitanya)",
    author_email="<vasantchaitanya@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[openai],
    keywords=['text to audio', 'audio', 'llm', 'openai','text'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
