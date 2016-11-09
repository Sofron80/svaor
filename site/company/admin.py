from django.contrib import admin

from .models import Category, Tovar, Page
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}  

class TovarAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)} 

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)} 

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tovar, TovarAdmin)
admin.site.register(Page, PageAdmin)


