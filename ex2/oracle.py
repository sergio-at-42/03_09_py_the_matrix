#!/usr/bin/env python3


from importlib import import_module
from types import ModuleType
import os


def check_package(package_name: str) -> ModuleType | None:
    package: ModuleType | None = None
    try:
        package = import_module(package_name)
    except (ImportError):
        print(f"{package_name} package not installed.")
        print(f"Installing with pip => pip install {package_name}")
        print("")
    return (package)


def value_in_dotenv(key: str) -> str:
    dotenv: ModuleType | None = check_package("dotenv")
    if dotenv:
        env_file: dict[str, str] = dotenv.dotenv_values()
        return (env_file[key])
    return ("")


def load_conf(conf: dict[str, str]) -> bool:
    dotenv: ModuleType | None = check_package("dotenv")
    if dotenv:
        if dotenv.load_dotenv():
            conf["MATRIX_MODE"] = os.getenv("MATRIX_MODE", "")
            conf["DATABASE_URL"] = os.getenv("DATABASE_URL", "")
            conf["API_KEY"] = os.getenv("API_KEY", "")
            conf["LOG_LEVEL"] = os.getenv("LOG_LEVEL", "")
            conf["ZION_ENDPOINT"] = os.getenv("ZION_ENDPOINT", "")
            return (True)
        else:
            print("No .env file found.")
            print("")
    return (False)


def oracle() -> None:
    conf: dict[str, str] = {}
    print("ORACLE STATUS: Reading the Matrix...")
    print("")
    if load_conf(conf):
        print("Configuration loaded:")
        print(f"Mode: {conf["MATRIX_MODE"] if conf["MATRIX_MODE"]
                       else "No mode selected"} Database: ", end="")
        if conf["DATABASE_URL"]:
            database: str = "local" \
                if conf["DATABASE_URL"].find("localhost") >= 0 else "distant"
            print(f"Connected to {database} instance")
        else:
            print("NOT Connected")
        print(f"API Access: {"NOT " if not conf["API_KEY"]
                             else ""}Authenticated")
        print(f"Log Level: {conf["LOG_LEVEL"].upper()}")
        print(f"Zion Network: {"Online" if conf["ZION_ENDPOINT"]
                               else "Offline"}")
        print("")

        print("Environment security check:")
        print(f"{"[KO]" if value_in_dotenv("API_KEY")
                 else "[OK] No"} hardcoded secrets detected")
        if (value_in_dotenv("MATRIX_MODE")
            and value_in_dotenv("DATABASE_URL")
            and not value_in_dotenv("API_KEY")
            and value_in_dotenv("LOG_LEVEL")
                and value_in_dotenv("ZION_ENDPOINT")):
            print("[OK] .env file properly configured")
        else:
            print("[KO] .env file NOT properly configured")
        if conf["MATRIX_MODE"] == "production":
            print("[OK] Production overrides available")
        else:
            print("[KO] Not in Production mode (Development mode activated)")
        print("")
        print("The Oracle sees all configurations.")
    else:
        print("No .env file loaded. Check error above.")
    print("")


if __name__ == "__main__":
    oracle()
