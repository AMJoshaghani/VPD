"""
Logger.py
could be used for any projects.
written by amjoshaghani

usage:
LoggerInstance.log(<text>, <place>
LoggerInstance.error(<text>, <place>))
LoggerInstance.warning(<text>, <place>)
"""

import sys
from dataclasses import dataclass

@dataclass
class Logger():
    # ascii colors:
    colors = {
                "red": u"\u001b[31m",
                "magenta": u"\u001b[35m",
                "yellow": u"\u001b[33m",
                "cyan": u"\u001b[36m",
                "green": u"\u001b[32m",
                "white": u"\u001b[37m",
                "reset": u"\u001b[0m"
            }

    # main function defenition:
    def _print(self: object, text: str, pos: str, type_: str, colors: list) -> None:
        pcolor: str = colors[0]  # primary color
        scolor: str = colors[1]  # secondary color
        tcolor: str = colors[2]  # third color
        reset: str = self.colors["reset"]  # reset
        texts: list = str(text).splitlines()
        
        for i in range(0, len(texts)):
            line: str = texts[i]
            if i == 0:
                print(f"{pcolor}({type_}){reset} from {scolor}{pos}{reset}:\t {tcolor}{line}")
            else:
                print(f"\t{line}")

            if i >= len(texts)-1:
                print(reset)

    def _generate_colors(self, colors: list) -> list:
        colours: list = []  # generate color codes from given name
        for c in colors:
            colours.append(self.colors[c])
        return colours

    def error(self: object, error: str, position: str) -> None:
        colors: list = self._generate_colors(["red", "magenta", "red"])
        self._print(error, position, "EE", colors)  # EE: error
        sys.exit(1)  # terminate the program

    def warning(self: object, error: str, position: str) -> None:
        colors: list = self._generate_colors(["yellow", "cyan", "yellow"])
        self._print(error, position, "WW", colors)  # WW: warning

    def log(self: object, log: str, position: str) -> None:
        colors: list = self._generate_colors(["cyan", "white", "green"])
        self._print(log, position, "LL", colors)  # LL: log

