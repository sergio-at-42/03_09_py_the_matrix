#!/usr/bin/env python3


import sys
import os
import site


def construct() -> None:
    # if hasattr(sys, "real_prefix")  or (sys.base_prefix != sys.prefix):
    venv_path: str = os.environ.get('VIRTUAL_ENV')   # ou sys.prefix
    if venv_path:
        print("MATRIX STATUS: Welcome to the construct")
        print("")
        print(f"Current Python: {sys.executable}")
        venv_name = os.path.basename(venv_path)
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {venv_path}")   # ou sys.prefix
        print("")
        print("SUCCESS: You’re in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print("")
        print("Package installation path:")
        venv_site_packages: list[str] = [p for p in site.getsitepackages() if "site-packages" in p and p.startswith(sys.prefix)]
        print(f"{venv_site_packages[0] if venv_site_packages else "Not Found..."}")
    else:
        print("MATRIX STATUS: You’re still plugged in")
        print("")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print("")
        print("WARNING: You’re in the global environment!")
        print("The machines can see everything you install.")
        print("")
        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print("")
        print("Then run this program again.")


if __name__ == "__main__":
    construct()
