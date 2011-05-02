from setuptools import setup, find_packages
setup(
    name = 'Pokedex',
    version = '0.1',
    zip_safe = False,
    packages = find_packages(),
    package_data = {
        'pokedex': ['data/csv/*.csv']
    },
    install_requires=[
        'SQLAlchemy>=0.6.6',
        'whoosh>=1.1.0',
        'markdown',
        'construct',
        'argparse',
    ],

    entry_points = {
        'console_scripts': [
            'pokedex = pokedex.main:main',
        ],
    },
)
