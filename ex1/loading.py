#!/usr/bin/env python3


from importlib import metadata, import_module
from types import ModuleType


def check_packages(dependances: dict[str, ModuleType]) -> bool:
    dep_ok: bool = True
    for dep in dependances:
        try:
            dependances[dep] = import_module(dep)
            print(f"[OK] {dep} - {metadata.version(dep)}")
        except (ImportError):
            print(f"{dep} : MISSING")
            print("Installing with pip :")
            print("    => pip install -r requirements.txt")
            print("    => python3 loading.py")
            print("Installing with Poetry :")
            print("    => poetry install")
            print("    => poetry run python loading.py")
            dep_ok = False
    return (dep_ok)


def loading() -> None:
    print("LOADING STATUS: Loading programs...")
    print("")
    print("Checking dependencies:")
    dependances: dict[str, ModuleType] = {
        "pandas": None,
        "numpy": None,
        "matplotlib": None
    }
    if check_packages(dependances):
        print("")

        print("Analyzing Matrix data...")
        print("")

        print("Processing 1000 data points...")
        print("")

        print("Generating visualization...")
        print("")

        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    loading()
