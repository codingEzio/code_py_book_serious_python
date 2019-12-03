### Libraries

- `distutils` <small>([_doc_](https://docs.python.org/3/library/distutils.html), [_tutorial_](https://docs.python.org/3/distutils/introduction.html))</small>
  1. A part of the _Python Standard Library_
  2. A better `distlib` <small>([_doc_](https://pythonhosted.org/distlib/tutorial.html), [_repo_](https://bitbucket.org/pypa/distlib/src/default/))</small> library _might_ replace it in the future.
  3. It could handle simple packaging and distribution.
- `setuptools` <small>([_doc_](https://setuptools.readthedocs.io/en/latest/setuptools.html#developer-s-guide), [_repo_](https://github.com/pypa/setuptools))</small>
  1. The **standard** for _advanced package installations_

### Have a taste of `setuptools`
> 
```bash
# Please make sure you alright got 'setuptools' & 'pbr' installed,
# also, create files like 'setup.py', 'setup.config' and 'README.rst'.
$ ls
├── setup.py        # initilize packaging script, like 'setuptools.setup(...)'
├── setup.config    # add meta-data (e.g. repo-link, author, license, url etc.)
├── README.rst

# Checking stuff
$ python3 setup.py --help                   # general help text
$ python3 setup.py --help-commands          # commands you actually would use

# Basic cmds you might use
$ python3 setup.py sdist                    # => a source distribution (tarball or zip)
$ python3 setup.py bdist                    # => a built(binary) distribution
$ python3 setup.py bdist_wininst            # => an executable installer for MS Windows         

# For the '.wheel' format
$ pip3 install wheel==0.33.6                # required by 'setuptools'
$ python3 setup.py bdist_wheel              # => a '.whl' distribution
$ python3 setup.py bdist_wheel --universal  # same as above, only use if u sup both 2&3
```

### A `.whl` file
- Wut
    - *Wheel is a great format for distributing ready­-to­-install libraries and applications*.
- PEPs
    - [PEP 427 -- The Wheel Binary Package Format 1.0](https://www.python.org/dev/peps/pep-0427/)
    - [PEP 491 -- The Wheel Binary Package Format 1.9](https://www.python.org/dev/peps/pep-0491/)
- Facts
    1. It can be installed via `pip` like other types
    2. It is just a zip file with a different extension
- Awesomeness
    > It doesn't require installation, you can *load* and *run* your code  
    > just by adding a **`/`** like this `python3 PKGNAME-xx-xx-xx-xx.whl/PKGNAME`
