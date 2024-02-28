# setup.py
from setuptools import setup, find_packages

setup(
    name='eaddaa-game',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'tea_weather_app==0.1.0',
    ],
    url='https://github.com/eaddaa/eaddaa_game',
    entry_points={
        'console_scripts': [
            'eaddaa-game=eaddaa_game.game_logic:play_game',
        ],
    },
    author='eaddaa',
    author_email='eaddaa@gmail.com',
    description='eaddaa-game_project',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
    project_urls={
        'Source': 'https://github.com/eaddaa/eaddaa_game',
    },
)
