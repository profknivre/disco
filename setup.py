# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['disco']

package_data = \
{'': ['*']}

install_requires = \
['redis>=2.10,<3.0']

setup_kwargs = {
    'name': 'disco',
    'version': '0.1.0',
    'description': 'very simple service discovery app',
    'long_description': None,
    'author': 'Grzegorz Zebrowski',
    'author_email': 'grzegorz.zebrowski@thrust.pl',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
}


setup(**setup_kwargs)
