import json
import pyperclip

text = input('Enter JSON string: ')

if not text.startswith('"'):
    text = '"' + text + '"'

loaded = json.loads(text)
mini = json.dumps(loaded, separators=(',', ':'))
mini = mini.replace('\\', '\\\\')
mini = mini.replace('"', '\\"')

print(mini)
pyperclip.copy(mini)
