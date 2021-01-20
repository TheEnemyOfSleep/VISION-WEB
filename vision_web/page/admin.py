from django.contrib import admin
from page.models import (
    Block,
    Element
)

admin.site.register(Element)


@admin.register(Block)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "note", "sorting")
