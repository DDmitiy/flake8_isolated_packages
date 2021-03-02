# flake8_isolated_packages

This *Flake8* plugin is for checking imports isolations.  
**One rule:** Any module from specified package could not be import in another package

# Quick Start Guide

1. Install ``flake8-isolated-packages`` from PyPI with pip::

        pip install flake8-isolated-packages

2. Configure a mark that you would like to validate::

        cd project_root/
        vi setup.cfg

3. Add to file following: 
   
        [flake8]  
        isolated_packages = service, tests  
        test_folders = tests

3. Run flake8::

        flake8 .

# flake8 codes

   * FIP100: You try to import from isolated package

# Settings

**isolated_packages**  
It specifies a list of folders, that cannot be imported outside of their package

**test_folders**  
It specifies a list of folders, that contains tests and in which can be imported something from even isolated packages
