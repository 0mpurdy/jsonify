import json
import pyperclip

minify = True
minifyOnly = True
jsonNewline = '\\r\\n'

text = input('Enter JSON string: ')

use_input_file = text == ""
if use_input_file:
    with open('input.json') as f:
        text = f.read()

text = text.rstrip("\n")

if minify:
    loaded = json.loads(text)
    mini = json.dumps(loaded, separators=(',', ':'))
else:
    mini = text

if not minifyOnly:
    mini = mini.replace('\\', '\\\\')
    mini = mini.replace('"', '\\"')
    mini = '"' + mini + '"'
    mini = mini.replace('\n', jsonNewline)

if use_input_file:
    with open('output.json', "w") as f:
        print(mini, file = f)
else:
    print(mini)

pyperclip.copy(mini)
