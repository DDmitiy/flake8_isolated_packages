from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='flake8-isolated-packages',
    packages=['./'],
    version='0.1.3',
    license='MIT',
    description='This flake8 plugin is for checking imports isolations.',
    long_description=long_description,
    author='Dudov Dmitriy (ddmitiy)',
    author_email='dudov.dm@gmail.com',
    url='https://github.com/DDmitiy/flake8_isolated_packages',
    keywords=['flake8', 'plugin', 'imports', 'packages', 'isolation'],
    install_requires=[
        'importlib-metadata',
        'flake8',
        'astpretty',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
