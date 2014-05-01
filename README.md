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
```bash  
$ python piplatest.py freeze  
```  
Generate `requirements.txt` without version info
<br>

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
<br>

```bash    
$ python piplatest.py install   
```  
Install from requirements.txt but ignore version info,i.e. use the latest version.
<br>

```bash    
$ python piplatest.py install -v django six  
```  
`django` and `six` will install the version specified in `requirements.txt`, others packages use the latest.