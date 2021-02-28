# flake8_isolated_packages

This *Flake8* plugin is for checking imports isolations.  
**One rule:** Any module from specified package could not be import in another package

# Quick Start Guide

1. Install ``flake8-isolated-packages`` from PyPI with pip::

        pip install flake8-isolated-packages

2. Configure a mark that you would like to validate::

        cd project_root/
        vi .flake8

3. Add to file following: 
   
        [flake8]
        isolated_packages = service, tests

3. Run flake8::

        flake8 .