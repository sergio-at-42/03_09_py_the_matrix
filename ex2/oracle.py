#!/usr/bin/env python3


import dotenv
import os, sys


def load_conf(conf: dict[str, str]) -> None:
    dotenv.load_dotenv()
    conf["MATRIX_MODE"] = os.getenv("MATRIX_MODE")
    conf["DATABASE_URL"] = os.getenv("DATABASE_URL")
    conf["API_KEY"] = os.getenv("API_KEY")
    conf["LOG_LEVEL"] = os.getenv("LOG_LEVEL")
    conf["ZION_ENDPOINT"] = os.getenv("ZION_ENDPOINT")


def oracle() -> None:
    conf: dict[str, str] = {}
    load_conf(conf)
    print("ORACLE STATUS: Reading the Matrix...")
    print("")
    print("Configuration loaded:")
    print(f"Mode: {conf["MATRIX_MODE"]}")
    print(f"Database: {conf["DATABASE_URL"]}")
    print(f"API Access: {conf["API_KEY"]}")
    print(f"Log Level: {conf["LOG_LEVEL"]}")
    print(f"Zion Network: {conf["ZION_ENDPOINT"]}")
    print("")

    print("Environment security check:")
    print(f"{"[OK] No" if conf["API_KEY"] else "[KO]"} hardcoded secrets detected")
    print("")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    oracle()
