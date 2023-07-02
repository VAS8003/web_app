from modeltranslation.translator import register, TranslationOptions

from main.models import Product, Cases


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'preview', 'content')


@register(Cases)
class CasesTranslationOptions(TranslationOptions):
    fields = ('title', 'preview', 'content')