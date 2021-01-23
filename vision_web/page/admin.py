from django.contrib import admin
from page.models import (
    Block,
    Component,
    ElementsRel,
    ButtonElement,
    LabelElement
)

admin.site.register(ElementsRel)
admin.site.register(Component)
admin.site.register(ButtonElement)
admin.site.register(LabelElement)


@admin.register(Block)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "note", "sorting")
