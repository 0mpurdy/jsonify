import pyperclip

text = input('Enter string: ')

use_input_file = text == ""
if use_input_file:
    with open('input.txt') as f:
        text = f.read()

text = text.replace('\\', '\\\\')
text = text.replace('"', '\\"')
text = text.replace('\n', '\\n')
text = '"' + text + '"'

if use_input_file:
    with open('output.txt', "w") as f:
        print(text, file = f)
else:
    print(text)

pyperclip.copy(text)
