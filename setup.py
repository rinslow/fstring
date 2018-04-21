"""Setup file for handling packaging and distribution."""
from setuptools import setup

setup(
    name='fstring',
    packages=['fstring'],
    version='1.5',
    description='Working with strings has never been prettier.',
    author='Dan Elkis',
    author_email='elkissdan@gmail.com',
    license='MIT',
    zip_safe=False,
    url='https://github.com/d-kiss/fstring',
    keywords=['string', 'fstring', 'formatting', 'inline', 'evaluation'],
    classifiers=[
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: PyPy',

    ],
)
