# JSON to Android Strings XML Converter

Converts a JSON array of objects into an Android `strings.xml` file.

## Usage

```bash
python json_to_android_strings.py <input.json>
```

The output XML file is saved in the same directory as the input file.

## Input Format

```json
[
  {
    "id": 1,
    "title": "Welcome",
    "description": "Hello World"
  }
]
```

## Output Format

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="title_1">Welcome</string>
    <string name="description_1">Hello World</string>
</resources>
```

## Dependencies

Install dependencies with:

```bash
pip install -r requirements.txt
```

### python-dotenv

The `.env` file is loaded automatically when using `python-dotenv`. Run:

```bash
python -m dotenv python json_to_android_strings.py <input.json>
```

## NixOS Development Environment

If using NixOS, enter the development shell with:

```bash
nix develop
```
