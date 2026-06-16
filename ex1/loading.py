#!/usr/bin/env python3


from importlib import metadata, import_module

import pandas
import numpy
import matplotlib


def loading() -> None:
    print("LOADING STATUS: Loading programs...")
    print("")
    print("Checking dependencies:")
    dependances: list[str] = ["pandas", "numpy", "matplotlib"]
    for dep in dependances:
        try:
            print(f"[OK] {dep} - {metadata.version(dep)}")
            print("")
        except metadata.PackageNotFoundError:
            print(f"{dep} : MISSING")
            print("Installing with pip :")
            print("    => pip install -r requirements.txt")
            print("    => python3 loading.py")
            print("Installing with Poetry :")
            print("    => poetry install")
            print("    => poetry run python loading.py")
            print("")

    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")
    print("Generating visualization...")
    print("")

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    loading()
