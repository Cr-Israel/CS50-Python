from pyfiglet import Figlet

import sys

figlet = Figlet()

fonts = figlet.getFonts()

if len(sys.argv) == 1:
    f = "standard"
else:
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage")
    if len(sys.argv) < 3:
        sys.exit("Invalid usage")
    if not (sys.argv[2] in fonts):
        sys.exit("Invalid usage")
    f = sys.argv[2]

figlet.setFont(font=f)

entry = str(input("Input: "))
serializedEntry = figlet.renderText(entry)
print(f"Output:\n{serializedEntry}")
