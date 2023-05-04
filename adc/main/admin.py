from django.contrib import admin

from .models import  *

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
class CaseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Product, ProductAdmin)
admin.site.register(Cases, CaseAdmin)
