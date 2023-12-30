from django.db import models
from django.urls import reverse_lazy


class ExampleModelChoice(models.IntegerChoices):
    GENERATED = 0, 'Generated'


class ExampleModel(models.Model):
    product_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'example_model'

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse_lazy('example_model-list')
