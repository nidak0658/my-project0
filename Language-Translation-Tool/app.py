import os
from google.cloud import translate_v2 as translate

# Replace with your own API key path
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/path/to/your/api/key.json'

# Initialize the translator
translator = translate.Client()

def translate_text(text, target_language):
    """
    Translates text to the target language.

    Args:
        text (str): The text to be translated.
        target_language (str): The language code of the target language.

    Returns:
        str: Translated text.
    """
    result = translator.translate(text, target_language=target_language)
    return result['translatedText']

# Example usage
text_to_translate = "Hello, how are you?"
target_language = "fr"  # Language code for French

translated_text = translate_text(text_to_translate, target_language)
print(f'Translation: {translated_text}')

