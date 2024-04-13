"""
# Scripts / Check stubs against FL Studio

Check to ensure that the stub code completely covers all functions in FL
Studio's library.
"""
import importlib
import inspect
import flapi


MODULES = [
    "arrangement",
    "channels",
    "device",
    "general",
    "launchMapPages",
    # "midi",
    "mixer",
    "patterns",
    "playlist",
    "plugins",
    "screen",
    "transport",
    "ui",
    # "utils",
]


LibraryItems = dict[str, list[str]]


def filter_module_items(items: list[str]) -> list[str]:
    """
    Filter items such that we only include the relevant ones
    """
    return list(filter(
        lambda name: not name.startswith('_'),
        items,
    ))


def generate_from_stubs(modules: list[str]) -> 'LibraryItems':
    """
    Generate collection of all items in the stub code
    """
    items = {}
    for mod in modules:
        items[mod] = filter_module_items(dir(importlib.import_module(mod)))
    return items


def generate_from_fl_studio(modules: list[str]) -> LibraryItems:
    """
    Generate collection of all items in FL Studio
    """
    # Connect to FL Studio
    if not flapi.enable():
        print("Couldn't connect to FL Studio")
        exit(1)

    flapi.fl_exec("import importlib")
    flapi.fl_exec(inspect.getsource(filter_module_items))
    flapi.fl_exec(inspect.getsource(generate_from_stubs))

    flapi.fl_eval(f"generate_from_stubs({modules})")

    return flapi.fl_eval(f"generate_from_stubs({modules})")


def diff(stubs: LibraryItems, fl: LibraryItems) -> bool:
    """
    Detect the difference between the API functions
    """
    found_diff = False

    for mod in stubs:
        stub_contents = stubs[mod]
        fl_contents = fl[mod]

        for item in stub_contents:
            if item not in fl_contents:
                print(f"++ {mod}.{item}")
                found_diff = True

        for item in fl_contents:
            if item not in stub_contents:
                print(f"-- {mod}.{item}")
                found_diff = True

    return found_diff


def main():
    stubs = generate_from_stubs(MODULES)
    fl = generate_from_fl_studio(MODULES)
    if diff(stubs, fl):
        print("Stub code not same as FL Studio libraries")
        exit(1)
    else:
        print("Stub code matches FL Studio libraries")


if __name__ == '__main__':
    main()
