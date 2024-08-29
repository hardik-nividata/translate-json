# translate-json
Translate the JSON based content using DeepL Translation API

## Project Setup

### Prerequisites

```
Python===3.11.1
```

## Installation

To work with this script you need to install dependencies library that are mentioned in requirements file. 
Also, you need a one Deepl API key to translate the content. You can gererate api key from [`DeepL API`](https://www.deepl.com/en/pro-api). Get more info please follow this [`DeepL Official Document`](https://developers.deepl.com/docs).

### Dependencies

To install all the required modules use `pip install -r requirements.txt` command.

```bash
  pip install -r requirements.txt
```

## Getting Started

To run this script run below command.

```bash
    python translate_json.py /path/to/json_file target_language
```

Both arguments are required. 
```
    Arguments: 
    * /path/to/json_file : mention the json file path
    * target_langugae: Give the 2 letter ISO language code [`Supported Languages`](https://developers.deepl.com/docs/resources/supported-languages#target-languages).
```
