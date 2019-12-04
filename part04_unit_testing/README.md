
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
$ pytest --verbose TESTS -m "KEYWORDS"
$ pytest --verbose TESTS -m "not KEYWORDS"
```