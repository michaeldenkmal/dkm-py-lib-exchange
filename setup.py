from setuptools import setup

setup(
    name='dkm_lib_exchange',
    packages=['dkm_lib_exchange'],
    description='Denkmal Exchange Server Utils',
    version='1.0',
    url='http://github.com/michaeldenkmal/dkm-py-lib-exchange',
    author='michael',
    author_email='michael@denkmal.at',
    keywords=['denkmal','exchange server'],
    install_requires=[
        "exchangelib"
    ]
    )