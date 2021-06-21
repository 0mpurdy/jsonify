import json
import pyperclip

text = input('Enter JSON string: ')

use_input_file = text == ""
if use_input_file:
    with open('input.json') as f:
        text = f.read()

text = text.rstrip("\n")

loaded = json.loads(text)
mini = json.dumps(loaded, separators=(',', ':'))
mini = mini.replace('\\', '\\\\')
mini = mini.replace('"', '\\"')
mini = '"' + mini + '"'

if use_input_file:
    with open('output.json', "w") as f:
        print(mini, file = f)
else:
    print(mini)

pyperclip.copy(mini)
