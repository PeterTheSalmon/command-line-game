"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['__main__.py']
DATA_FILES = ['Bloodmoon Game Over.png',
              'bloodmoonMonster.png',
              'bloodmoonMonster2.png',
              'bloodmoonMonster3.png',
              'bloodmoonMonster4.png',
              'bloodmoonMonster5.png',
              'bloodmoonMonster6.png',
              'player.png',
              'VictoryNew.png']
OPTIONS = {}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)