
### Issues you might encounter
- Weird ` PytestUnknownMarkWarning: Unknown pytest.mark.dicttest - is this a typo?`
    >
    ```ini
    [pytest]
    markers =
        skip        # built-in
        dicttest    # user-defined
    ```

### Common-used test commands

>
```bash
# Basic
$ pytest --verbose TESTS            # either is fine
$ pytest --verbose PATH/TO/TESTS    # it could detect all of them       

# Run particular tests
$ pytest --verbose TESTS -k "SPECFIC_FUNCTION"

# Run particular tests based on keywords
$ pytest --verbose TESTS -m "KEYWORD"               # tests with this keyword
$ pytest --verbose TESTS -m "not KEYWORD"           # any tests except this one
$ pytest --verbose TESTS -m "KEYWORD or KEYWORD"    # tests with either keywords
$ pytest --verbose TESTS -m "KEYWORD and KEYWORD"   # tests with both|all the keywords
```

### Advaned test commands|usage

>
```bash
$ pip3 install pytest-xdist==1.30.0

$ pytest --verbose TESTS --looponfail               # re-run the test after file changes
$ pytest --verbose TESTS --numprocesses 4           # run ur tests using N processes
$ pytest --verbose TESTS --numprocesses auto        # a more robust|clever way
```
