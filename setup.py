from setuptools import setup, find_packages

setup(
    name='eaddaa-game',
    version='0.1.3',
    packages=find_packages(),
    install_requires=[
        'tea_weather_app==0.1.0',
    ],
    entry_points={
        'console_scripts': [
            'eaddaa-game=eaddaa_game.game_logic:play_game',
        ],
    },
    author='eaddaa',
    author_email='eaddaa@gmail.com',
    description='eaddaa-game_project',
    bugtrack_url='https://github.com/eaddaa/eaddaa_game',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
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
