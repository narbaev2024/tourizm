from modeltranslation.translator import TranslationOptions, register
from .models import Landmark

@register(Landmark)
class LandmarkTranslationOptions(TranslationOptions):
    fields = ('description',)
