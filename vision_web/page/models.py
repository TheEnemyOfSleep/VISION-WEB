from django.db import models


class Block(models.Model):

    name = models.CharField(max_length=100, unique=True)
    elements = models.ManyToManyField('Element', blank=True)
    sub_block = models.ManyToManyField(
        'self',
        blank=True,
        related_name='root',
        symmetrical=False
    )
    sorting = models.PositiveIntegerField(default=0)
    id_attr = models.CharField(max_length=100, blank=True)
    classes = models.CharField(max_length=200, blank=True)
    extra_attrs = models.TextField(blank=True)
    style = models.TextField(blank=True)

    # Simple note for understanding what block is this
    note = models.CharField(max_length=150, blank=True)

    class Meta:
        ordering = ['-sorting']
        verbose_name = 'block'
        verbose_name_plural = 'block'

    def __str__(self):
        return self.name


class Element(models.Model):

    name = models.CharField(max_length=100, unique=True)
    sorting = models.PositiveIntegerField(default=0)
    content = models.TextField()
    style = models.TextField(blank=True)
    script = models.TextField(blank=True)

    def __str__(self):
        return self.name

