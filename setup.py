# :coding: utf-8
# :copyright: Copyright (c) 2021 Lluis Casals Marsol
# Please see the LICENSE file that should have been included as part of this
# package.

import os

from setuptools import setup, find_packages

from pkg_resources import get_distribution, DistributionNotFound


ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
SOURCE_PATH = os.path.join(ROOT_PATH, 'source')
README_PATH = os.path.join(ROOT_PATH, 'README.rst')

try:
    release = get_distribution('covalent-python-api').version
    # take major/minor/patch
    VERSION = '.'.join(release.split('.')[:3])
except DistributionNotFound:
    # package is not installed
    VERSION = 'Unknown version'


version_template = '''
# :coding: utf-8
# :copyright: Copyright (c) 2021 Lluis Casals Marsol
# Please see the LICENSE file that should have been included as part of this
# package.

__version__ = {version!r}
'''

# Call main setup.
setup(
    name='covalent-python-api',
    description='Python API for Covalent.',
    author='Lluis Casals Marsol',
    author_email='ktmlleska@gmail.com',
    url='https://bitbucket.org/lluisBrokenC/covalent_python_api',
    long_description=open(README_PATH).read(),
    license='GNU General Public License v3.0 (GPLv3)',
    keywords='covalent, python, api',
    packages=find_packages(SOURCE_PATH),
    project_urls={
        "Documentation": "https://covalent-python-api.readthedocs.io/en/latest/",
        "Covalent API Documentation": "https://www.covalenthq.com/docs/api/",
        "Covalent Homepage": "https://www.covalenthq.com/",
    },
    package_dir={
        '': 'source'
    },
    use_scm_version={
        'write_to': 'source/covalent_api/_version.py',
        'write_to_template': version_template,
    },
    setup_requires=[
        'docutils < 0.17',
        'sphinx >= 1.2.2, < 1.6',
        'sphinx_rtd_theme >= 0.1.6, < 1',
        'setuptools>=47.1.0',
        'setuptools_scm'
    ],
    install_requires=[
        'requests >= 2, <3',
    ],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3'
    ],
    zip_safe=False,
    python_requires=">=3.7.6, <4.0"
)
