# setup.py
from setuptools import setup, find_packages

setup(
    name='eaddaa-game',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'tea_weather_app==0.1.0',
    ],
    url='https://github.com/eaddaa/eaddaa-game',  # Buraya kendi Git deposunuzun URL'sini ekleyin
    entry_points={
        'console_scripts': [
            'eaddaa-game=eaddaa_game.game_logic:play_game',
        ],
    },
)
