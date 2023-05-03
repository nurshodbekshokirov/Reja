from modeltranslation.translator import translator, TranslationOptions
from .models import Reja

class RejaTranslationOptions(TranslationOptions):
    fields = ('sarlavha', 'batafsil', 'holat')





translator.register(Reja, RejaTranslationOptions)