# setup.py
from setuptools import setup, find_packages

setup(
    name='eaddaa-game',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests==2.26.0',
    ],
    entry_points={
        'console_scripts': [
            'eaddaa-game=eaddaa_game.game_logic:play_game',
        ],
    },
)
