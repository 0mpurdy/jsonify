import json
import pyperclip

text = input('Enter encoded JSON string: ')

use_input_file = text == ""
if use_input_file:
    with open('input.json') as f:
        text = f.read()

text = text.rstrip("\n")

if text.startswith('"'):
    text = text[1:-1]

text = text.replace('\\\\', '\\')
text = text.replace('\\"', '"')
loaded = json.loads(text)

pretty = json.dumps(loaded, indent = 4)

if use_input_file:
    with open('output.json', "w") as f:
        print(pretty, file = f)
else:
    print(pretty)

pyperclip.copy(pretty)
