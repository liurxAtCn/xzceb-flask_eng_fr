"""
translate via waston
"""
import json
import os
import traceback
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
CUR_VERSION = '2022-08-30'

def init_translator():
    """init instance"""
    authenticator = IAMAuthenticator( apikey)
    language_translator = LanguageTranslatorV3(
        version= CUR_VERSION,
        authenticator=authenticator
    )
    language_translator.set_service_url( url)
    return language_translator

language_translator = init_translator()

def parse_context( resp_dict):
    """parse the body from waston translator"""
    try :
        for ent in resp_dict['translations'] :
            if isinstance( ent, dict):
                if 'translation' in ent :
                    return ent['translation']
    except Exception:
        print( 'parseContext exception occure')
        print(traceback.format_exc())
    return ''

def englishToFrench( englishText):
    """
    english word to french
    """
    if englishText == '' :
        return  ''
    
    try:
        resp = language_translator.translate(
        text= englishText,
        model_id='en-fr').get_result()

        frenchText = parse_context( resp)

        return frenchText
    except Exception:
        print( 'englishToFrench exception occure,input:{}', englishText)
        print(traceback.format_exc())
        return ''

def frenchToEnglish(frenchText):
    """
    french word to english
    """
    if frenchText == '' :
        return  ''
    try:
        resp = language_translator.translate(
        text= frenchText,
        model_id='fr-en').get_result()

        englishText = parse_context( resp)

        return englishText
    except Exception:
        print( 'frenchToEnglish exception occure,input:{}', frenchText)
        print(traceback.format_exc())
        return ''
