# jsonify

Tool to convert between string encoded json object and a json object

e.g.

```
"{\"prop\":\"test\"}" <---> {"prop":"test"}
```

## Building

Create python venv and activate (instructions assume powershell)

```ps1
python -m venv .
Scripts/Activate.ps1
```

Install pip requirements

```ps1
pip install -r requirements.txt
```

Run script

```ps1
python jsonify.py
```

## Output

The output is printed to the console as well as copied to clipboard
