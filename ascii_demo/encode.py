""" convert a pyfiglet font into json
"""

import json
import re
from pyfiglet import Figlet
import os

def main():
    chars = {}
    f = Figlet(font="univers")
    for x in range(33, 127):
        lines = f.renderText(chr(x)).splitlines()
        chars[x] = lines
    print(json.dumps(chars))

main()