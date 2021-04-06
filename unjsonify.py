import json
import pyperclip

text = input('Enter encoded JSON string: ')

if text.startswith('"'):
    text = text[1:-1]

text = text.replace('\\\\', '\\')
text = text.replace('\\"', '"')
loaded = json.loads(text)

pretty = json.dumps(loaded, indent = 4)

print(pretty)
pyperclip.copy(pretty)
