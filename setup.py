from setuptools import setup

setup(
    name='newsservice',
    packages=['newsservice'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)