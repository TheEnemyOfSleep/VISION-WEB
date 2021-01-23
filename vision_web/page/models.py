from django.db import models
from django.core.exceptions import ValidationError


class Block(models.Model):

    name = models.CharField(max_length=100, unique=True)
    sorting = models.PositiveIntegerField(default=0)
    elements = models.ManyToManyField('ElementsRel', blank=True)
    components = models.ManyToManyField('Component', blank=True)
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

    # Simple note for understanding what block is this
    note = models.CharField(max_length=150, blank=True)

    class Meta:
        ordering = ['-sorting']
        verbose_name = 'block'
        verbose_name_plural = 'block'

    def __str__(self):
        return self.name


class Component(models.Model):

    name = models.CharField(max_length=100, unique=True)
    sorting = models.PositiveIntegerField(default=0)
    content = models.TextField()


    elements = models.ManyToManyField('ElementsRel', blank=True)
    sub_component = models.ManyToManyField(
        'self',
        blank=True,
        related_name='root',
        symmetrical=False
    )


class ElementsRel(models.Model):

    TYPE_CHOISES = [
        ('button_elem', 'Button'),
        ('label_elem', 'Label'),
    ]
    field_type = models.CharField(
        max_length=15, 
        choices=TYPE_CHOISES,
        default='button_elem'
    )

    sorting = models.PositiveIntegerField(default=0)

    button_elem = models.ForeignKey(
                                    'ButtonElement',
                                    on_delete=models.CASCADE,
                                    related_name='elements',
                                    blank=True,
                                    null=True
                                    )
    label_elem = models.ForeignKey(
                                    'LabelElement',
                                    on_delete=models.CASCADE,
                                    related_name='elements',
                                    blank=True,
                                    null=True
                                    )


    def get_type_field_choice(self):
        for choice in self.TYPE_CHOISES:
            if self.get_field_type_display() in choice:
                current_choice = choice[0]
                return current_choice
        return None


    def clean(self, *args, **kwargs):
        
        if getattr(self, self.get_type_field_choice()) is None:
            raise ValidationError('Current element cannot be blank')
        super(ElementsRel, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        FOREIGN_FIELDS = [
            str(key).split('.')[-1]
            for key 
            in self._meta.fields
            if key.get_internal_type() == 'ForeignKey'
        ]

        for field in FOREIGN_FIELDS:
            if self.get_type_field_choice() != field:
                setattr(self, field, None)
        super(ElementsRel, self).save(*args, **kwargs)


class ElementMixin(models.Model):

    attrs = models.TextField(blank=True)
    style = models.TextField(blank=True)
    script = models.TextField(blank=True)


    class Meta:
        abstract = True


class ButtonElement(ElementMixin):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class LabelElement(ElementMixin):
    label = models.CharField(max_length=150)

    def __str__(self):
        return self.label