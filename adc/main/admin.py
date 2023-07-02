from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import  *

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    prepopulated_fields = {"slug": ("title",)}
@admin.register(Cases)
class CaseAdmin(TranslationAdmin):
    prepopulated_fields = {"slug": ("title",)}

# admin.site.register(Product, TranslationAdmin)
# admin.site.register(Cases, CaseAdmin)
