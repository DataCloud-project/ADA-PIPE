from setuptools import setup

setup(
    name='json_utils',
    packages=['templates', 'static', 'test'],
    include_package_data=True,
    install_requires=[
        'flask',
],)