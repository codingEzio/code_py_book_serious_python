# About `import`

- `import os <> os = **import**("os")`
- `import itertools as it <> it = **import**("itertools")`

# Module `sys`

- `sys.modules['MODULE'] # where it is`
- `sys.modules.keys() # list of loaded modules`

# Import path

```
    $ PYTHONPATH=/rand/location python3
    >>> import sys
    >>> '/rand/location' in sys.path        # top

    $ python3
    >>> import sys
    >>> sys.path.append('/rand/location')   # bottom
```

# Useful built-in libs (do try them out)

```
abc                 a contract between the class impl & the callers (like interface)
atexit              register funcs when it exists
argparse            parsing cmdline args
bisect              bisection algorithms for sorting lists
calender            date-related funcs
datetime            handling dates & times
codecs              funcs for encoding/decoding data
collections         a variety of data structures
copy                copying data
concurrent          funcs for asynchronous computation
fnmatch             matching Unix-style filename patterns
glob                matching Unix-style path patterns
shutil              high-level file funcs
io                  handling I/O streams
csv                 r/w CSV files
json                r/w data in JSON format
multiprocessing     run multiple subproccess & while makes them look like threads
operator            implementing the basic operators
sched               an event scheduler without using multithreading
select              provide access to select/poll for creating event loops
signal              funcs for handling POSIX signals
tempfile            create temporary files and dirs
threading           high-level threading functionality
uuid                generate UniversallyUniqueIDentifiers (UUIDs)
```

# External libraries safety checklist

- Python 3 compatibility
- active development
- active maintenance
- License
- API compatibility commitment

# Protect your code with an API wrapper

- Simply put

  > It's like builting a bridge between the 3rd-party lib between your
  > own code. If something goes wrong, you can easily switch to other libs
  > instead of rewritten a huge parts of your program.

# Command `pip`

- `pip install -e .`
  - what does it do
    - install a project from a local path or VCS url
    - this is quite useful when the version hasn't been published <small>(to _pypi.org_)</small> yet
  - details
    - do note that it doesn't copy the dir, it creates an `egg-link` in the `site-packages`
      1. check path: `which python` or `pipenv --where` if you're using _pipenv_
      2. check file: `YOUR_PY_PATH/.../lib/pythonX.Y/site-packages/THE_EGGLINK_FILE`
      3. also you'd check `python -c "import sys; print(sys.path[-1]);"` (pkg path)
  - speed
    - Directly installing from [_pypi_](https://pypi.org) is the fastest way where a _wheel_ is available
    - other than that, _tarball_ is also not a bad idea (installed to PYPATH/`src`)
      - e.g. `pip install https://github.com/cranndarach/lexlib/archive/2.2.1.tar.gz#egg=lexlib`
      - and the _latest_ `pip install -e git+https://github.com/cranndarach/lexlib\#egg=lexlib`
  - steps
    1. `$ git clone https://github.com/henriquebastos/python-decouple/` <small>(just for example)</small>
    2. `$ cd python-decouple`
    3. `$ pip install -e .` <small>(boom, you got the package!)</small>

# Principle

- _Single Responsibility Principle_
  > think about what values can be stored in an instance and used by the methods
  > versus what needs to be passed to each method every time (the latter is _<q>bad</q>_)
- personal opinions on _common-programming errors_
  - use native impl instead of on your own: e.g. `itertools.chain()`
  - use [generator expressions](https://realpython.com/introduction-to-python-generators/)<small>(_realpython_)</small> instead of list comprehensions

# Documentation

- _Sphinx_ setup
  - Try
    - `$ pipenv install sphinx==2.2.1` (currently the latest ver)
    - `$ sphinx-quickstart`
      - `conf.py`: required conf file
      - `index.rst`: kinda the homepage for your doc
    - `$ sphinx-build [..]source [..]build` (depends on where you at)
      - now you can open the generated `index.html` to see the result!
  - Online editors <small>(might be down at anytime)</small>
    - [https://livesphinx.herokuapp.com/](https://livesphinx.herokuapp.com/)
    - [http://rst.ninjs.org/?theme=nature#](http://rst.ninjs.org/?theme=nature#)
  - More
    - [ReStructuredText syntax](http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html)
    - [A sample of RestructedText](https://github.com/lsegal/atom-rst-preview/blob/master/sample.rst)
    - [Perfect intro for those who havn't heard of _Sphinx_](https://speakerdeck.com/stephenfin/who-needs-pandoc-when-you-have-sphinx) <small>(slides on [_Speakdeck_](https://speakerdeck.com))</small>
    - And of course, the content in this book is pretty good as well.
