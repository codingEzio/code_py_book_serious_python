import atexit


def goodbye_usingregister(name):
    print(f"Farewell, {name}! (register)")


@atexit.register
def goodbye_usingdecorator():
    print(f"Farewell, (decorator) (no params allowed)")


atexit.register(goodbye_usingregister, name="Poli")
