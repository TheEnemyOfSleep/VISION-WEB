from django.contrib import admin
from page.models import (
    Block,
    Element
)

admin.site.register(Block)
admin.site.register(Element)


class BlockOptionInline(admin.TabularInline):
    model = Block
    fields = ('sorting', 'name')
