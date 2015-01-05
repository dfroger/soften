from setuptools import setup

setup(
    name = 'soften',
    version = '0.0.1',
    description = 'Change hard links to symbolic links',
    url = 'https://github.com/dfroger/soften',
    packages = ['soften',],
    entry_points = {
        'console_scripts': [
            'soften = soften.soften:main',
        ],
    },
    license = 'GPL V3',
    author = 'David Froger',
    author_email = 'david.froger@inria.fr',
)
