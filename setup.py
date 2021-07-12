"""Setup file for handling packaging and distribution."""
from setuptools import setup

setup(
    name='fstring',
    packages=['fstring'],
    version='1.7.5',
    description='Working with strings has never been prettier.',
    long_description=open("README.md", "rt").read(),
    author='Dan Elkis',
    author_email='elkissdan@gmail.com',
    license='MIT',
    zip_safe=False,
    install_requires=['astroid'],
    url='https://github.com/rinslow/fstring',
    keywords=['string', 'fstring', 'formatting', 'inline', 'evaluation'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
