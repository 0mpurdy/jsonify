import json
import pyperclip

text = input('Enter JSON string: ')
loaded = json.loads(text)
mini = json.dumps(loaded, separators=(',', ':'))
mini = mini.replace('"', '\\"')

print(mini)
pyperclip.copy(mini)
