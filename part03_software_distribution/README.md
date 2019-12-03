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


### Playing with [pypi.org]()
- Setup
    1. Register an account on [test.pypi.org](https://test.pypi.org/)
    2. Add `.pypirc` to your `$HOME`
        ```toml
        [distutils]
        index-servers = testpypi

        [testpypi]
        username = USERNAME
        password = PASSWORD
        repository = https://testpypi.python.org/pypi
        ```
    3. Upload your package
        ```bash
        $ pip3 install twine==3.1.1
        $ twine upload --repository-url https://test.pypi.org/legacy/ YOUR_PACKAGE
        ```
- Notes
    - Unfortunately, I encounterd enormous errors along the way. Still cannot get it right!
        - Also, do note that the examples which the author puts had been already out-dated.
        - The one I was trying is *testpypi* plus `twine`, well, I *failed* anyway.
    - Here's some links might be useful for you
        - [Using TestPyPI](https://packaging.python.org/guides/using-testpypi/)
        - [Tutorial on `twine`](https://pypi.org/project/twine/)
        - [Configuring a .pypirc File for Easier Python Packaging](https://truveris.github.io/articles/configuring-pypirc/)
        - [Github Issue - testpypi deployment fails (deprecated API) ](https://github.com/gcovr/gcovr/issues/197)
        - [Github Issue - Cannot upload using 1.9.1, 400 or 405 client errors](https://github.com/pypa/twine/issues/289)
        - [Github Issue - Better error messages when metadata does not validate](https://github.com/pypa/warehouse/issues/2668)
        - [stackoverflow - 400 ERROR: Invalid URI when uploading new PyPI package (twine)](https://stackoverflow.com/questions/44961730/400-error-invalid-uri-when-uploading-new-pypi-package-twine)
    - For the `.pypirc` part
        - You can generate a token on [test.pypi.org](https://test.pypi.org/manage/account/token/)
        - then replace the old `username`, `password` with this
            ```toml
            username = __token__
            password = pypi-LOOOOONG_TOKEN
            ```
