from django.contrib import admin

from .models import *


@admin.register(MagazineInfo)
class MagazineInfoAdmin(admin.ModelAdmin):
    list_display = ('title', )


@admin.register(EquipmentInfo)
class EquipmentInfoAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(EquipmentInfoItems)
class EquipmentInfoItemsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    list_display = ('title', )


@admin.register(EquipmentUseful)
class EquipmentUsefulAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(FavoriteEquipment)
class FavoriteEquipmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')


@admin.register(EquipmentCategory)
class EquipmentCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )

    # def display_equipments(self, obj):
    #     return ', '.join([ equ.name for equ in obj.equipments.all()[:3] ])
