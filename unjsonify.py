import json
import pyperclip

text = input('Enter encoded JSON string: ')
text = text.replace('\\"', '"')
loaded = json.loads(text)

pretty = json.dumps(loaded, indent = 4)

print(pretty)
pyperclip.copy(pretty)
