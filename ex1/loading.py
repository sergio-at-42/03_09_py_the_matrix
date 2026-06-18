#!/usr/bin/env python3


from importlib import metadata, import_module
from types import ModuleType


def check_package(pack_name: str) -> ModuleType | None:
    pack: ModuleType | None = None
    try:
        pack = import_module(pack_name)
    except (ImportError):
        print(f"{pack_name} : MISSING")
        print("Installing with pip :")
        print("    => pip install -r requirements.txt")
        print("    => python3 loading.py")
        print("Installing with Poetry :")
        print("    => poetry install")
        print("    => poetry run python loading.py")
        print("")
    else:
        assert pack.__package__ is not None
        print(f"[OK] {pack.__name__} - {metadata.version(pack.__package__)}")
    return (pack)


def loading() -> None:
    print("LOADING STATUS: Loading programs...")
    print("")
    print("Checking dependencies:")
    pandas: ModuleType | None = check_package("pandas")
    numpy: ModuleType | None = check_package("numpy")
    pyplot: ModuleType | None = check_package("matplotlib.pyplot")

    if pandas and numpy and pyplot:
        print("")

        print("Analyzing Matrix data (numpy)...")
        rng = numpy.random.default_rng()
        matrix_numpy = rng.integers(low=0, high=100, size=(100, 10))
        print(f"Lignes / Colonnes : {matrix_numpy.shape}")
        print(f"Nombre de dimension : {matrix_numpy.ndim}")
        print(f"Nombre total d'éléments : {matrix_numpy.size}")
        print(f"Type des éléments : {matrix_numpy.dtype}")
        print("")

        print("Processing 1000 data points (pandas)...")
        matrix_pandas = pandas.DataFrame(matrix_numpy)
        print(matrix_pandas)
        print(f"Lignes / Colonnes : {matrix_pandas.shape}")
        print("")

        print("Generating visualization (matplotlib)...")
        pyplot.plot(matrix_numpy)
        pyplot.title("Graphique complètement stupide")
        pyplot.savefig("matrix_analysis.png")
        pyplot.show()
        print("")

        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    loading()
