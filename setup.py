"""
Recursion in Python
---------

Recursion is a method of solving problems that involves breaking a problem down
into smaller and smaller subproblems until you get to a small enough problem
that it can be solved trivially. Usually recursion involves a function calling
itself. While it may not seem like much on the surface, recursion allows us to
write elegant solutions to problems that may otherwise be very difficult to
program.

This python program contains several solutions to common problems using recursion.

Other Links
```````````
* `development version
  <http://github.com/rahulnadella/calculator>`
"""

from setuptools import setup

setup(
    name='Recursion',
    version='1.0.0',
    url='http://github.com/rahulnadella/Recursion-Python',
    license='BSD',
    author='Rahul Nadella',
    author_email='rahulnadella@yahoo.com',
    description='Solutions to common problems using recursion',
    long_description=__doc__,
    py_modules=['recursion'],
    zip_safe=False,
    platforms='any',
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
