"""This file creates an instance of the IBM Watson API and passes two translating
functions. One to translate from english to french, the other french to english"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('iDcu4IuOwyeQrN72qvMZOxMYhC45X3aI7hpQsfQGMnfL')
language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/c70e8e1d-2874-4927-bf13-69a4d6c9d192')

def english_to_french(english_text):
    """Translates from english to french"""
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """Translates from french to english"""
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text

