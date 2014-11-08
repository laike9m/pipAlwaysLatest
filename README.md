Introduction
------------
pipAlwaysLatest is a **wrapper** around [`pip`](https://pypi.python.org/pypi/pip), so you must have pip installed or using Python3.4 which has pip installed by default.  
The reason I wrote this is sometimes I find it hard to install the latest version of packages using requirements.txt in that it always set specific versions. For most third-party packages, their existing APIs are stable, so installing the latest version is safer than you might think. Therefore I wrote this to help me do this, and in case certain version of packages are necessary, it's also possible to install them according to versions in requirements.txt by adding package name as argument.

Usage
-----
    usage: piplatest.py [-h] [-v USE_VERSION [USE_VERSION ...]] method
    
    pip install/freeze latest version
    
    positional arguments:
      methodmethod you want to apply, install/freeze
    
    optional arguments:
      -h, --helpshow this help message and exit
      -v USE_VERSION [USE_VERSION ...], --version-packages USE_VERSION [USE_VERSION ...]
    specify packages that will reserve version when
    generating requirements or install from requirements

Example
-------
### `pip freeze` wrapper

1. Generate `requirements.txt` without version info:
    ```bash  
    $ python piplatest.py freeze  
    ```  

2. Generate `requirements.txt` and keep some packages' version info:
    ```bash    
    $ python piplatest.py freeze -v django six   
    ```  
    `django` and `six` will keep version info in `requirements.txt`:  
    
        pkgA
        django==1.6.3
        ...
        six==1.4.1
        pkgB
        ...

### `pip install -r` wrapper
1. Install from `requirements.txt` using the latest version.  
    ```bash    
    $ python piplatest.py install   
    ```  
    Make sure you have a `requirements.txt` in the current working directory.

2. Install from `requirements.txt` using the latest version except for some packages:
    ```bash    
    $ python piplatest.py install -v django six  
    ```  
    For this case, `django` and `six` will install the version specified in `requirements.txt`, others packages use the latest.
