import json
from typing import Dict, List
import subprocess
import pathlib
import argparse


def _flatten_keys(contents: List) -> List:
    new_contents = []
    for item in contents:
        value = item["value"]
        name = item["name"]
        for key in item["keys"]:
            new_contents.append({"value": value, "name": name, "key": key})
    return new_contents


def _format_line(item: Dict) -> str:
    return f"{item['value']:3.3s} {item['key']:12.12s} {item['name']:30.30s}"


def _format_contents(contents: List) -> str:
    return "\n".join([_format_line(item) for item in contents])


def _wtype(text: str):
    subprocess.run(["wtype", text])


def _parse_output(output: str) -> str:
    return output.strip().split(" ")[0]


def _parse_args():
    """Parse command line arguments"""
    # optional argument for indicating matching mode
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-m",
        "--matching",
        default="fuzzy",
        choices=["fuzzy", "normal", "regex", "glob", "prefix"],
        help="Rofi matching mode, see rofi -h",
    )
    return parser.parse_args()


def main():
    args = _parse_args()
    with open(
        pathlib.Path.home().joinpath(
            ".local", "share", "mbc-unicode-input", "symbols.json"
        )
    ) as f:
        json_raw = f.read()
        contents = _flatten_keys(json.loads(json_raw))
        formatted = _format_contents(contents)
        output = subprocess.run(
            ["rofi", "-dmenu", "-matching", args.matching],
            input=str.encode(formatted),
            stdout=subprocess.PIPE,
        ).stdout.decode("utf-8")
        if len(output) > 0:
            _wtype(_parse_output(output))
