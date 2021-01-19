from django.db import models
from sort_order_field import SortOrderField

from django.utils.translation import ugettext_lazy as _


class Block(models.Model):

    name = models.CharField(max_length=100, unique=True)
    elements = models.ManyToManyField('Element', blank=True)
    sub_block = models.ManyToManyField(
        'self',
        blank=True,
        related_name='root',
        symmetrical=False
    )
    id_attr = models.CharField(max_length=100, blank=True)
    classes = models.CharField(max_length=200, blank=True)
    extra_attrs = models.TextField(blank=True)
    style = models.TextField(blank=True)
    sorting = models.PositiveIntegerField(default=0)

    # Simple note for understanding what block is this
    note = models.CharField(max_length=150, blank=True)

    def is_root(self, root=None):
        return len(self.root.all())

    class Meta:
        ordering = ['-sorting']
        verbose_name = _('block')
        verbose_name_plural = _('block')

    def __str__(self):
        return self.name


class Element(models.Model):

    name = models.CharField(max_length=100, unique=True)
    sorting = models.IntegerField(default=0)
    content = models.TextField()
    style = models.TextField(blank=True)
    script = models.TextField(blank=True)

    def __str__(self):
        return self.name
