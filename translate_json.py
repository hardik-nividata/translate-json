"""
This python pacakge is used to translate the json data into any language using DeepL translator.
"""

import json, sys, os
import deepl
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()


def translate_str(text, target_lang, *args,):
    try:
        result = translator.translate_text(text,target_lang=target_lang, formality="more", preserve_formatting=True)
        return result.text
    except Exception as e:
        print(e)
        return None
    

def translate_dict(data, target_language):
    try:
        if isinstance(data, dict):
            return {key: translate_dict(value, target_language) for key, value in data.items()}
        elif isinstance(data, list):
            return [translate_dict(item, target_language) for item in data]
        elif isinstance(data, str):
            return translate_str(data, target_language)
        else:
            return data
    except Exception as e:
        print(e)
        return None

def translate_json_data(input_file, target_language='EN-US'):
    try:
        print("JSON FILE READING...")
        with open(input_file, 'r', encoding='utf-8') as infile:
            data = json.load(infile)
        
        # Translate the content
        print("JSON FILE TRANSLATING...")
        translated_data = translate_dict(data, target_language)

        # Write the translated data to the output JSON file
        output_file = f"translated/{input_file}"
        if not os.path.exists(output_file):
            os.makedirs(os.path.dirname(output_file), exist_ok=True, mode=0o766)
        
        print("TRANSLATED JSON FILE WRITING...")
        with open(output_file, 'w', encoding='utf-8') as outfile:
            json.dump(translated_data, outfile, ensure_ascii=False, indent=4)
            
    except Exception as e:
        print(e)
        return None


if __name__ == "__main__":
    try:
        auth_key = os.getenv("DEEPL_API_KEY")  # Replace with your key
        print(auth_key)
        translator = deepl.Translator(auth_key)
        arguments = sys.argv[1:]
        if (len(arguments) <= 0):
            print("NO INPUT PASSED!")
        else:
            input_file = arguments[0]
            target_language = arguments[1]
            translate_json_data(input_file, target_language)
    except Exception as e:
        print(e)
