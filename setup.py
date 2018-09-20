from setuptools import setup

setup(
    name='flask-mongokat',
    version='1.0',
    url='https://github.com/FranciscoCarbonell/flask-mongokat',
    license='MIT',
    author='Francisco Carbonell',
    author_email='francabezo@gmail.com',
    description='Basic mongokat extension',
    py_modules=['flask_mongokat'],
    zip_safe=False,
    include_package_data=False,
    platforms='any',
    install_requires=['Flask','mongokat','pymongo']
)
