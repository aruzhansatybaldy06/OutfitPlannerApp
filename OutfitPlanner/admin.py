from django.contrib import admin

from OutfitPlanner.models import Clothes, Category

# Register your models here.
admin.site.site_header = 'Outfit Planner'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


class ClothAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')


admin.site.register(Clothes, ClothAdmin)
admin.site.register(Category, CategoryAdmin)
