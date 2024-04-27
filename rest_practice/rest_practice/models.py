from django.core.validators import MinValueValidator
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255, default='')
    slug = models.SlugField(default='')
    description = models.TextField(null=True, blank=True, default='')
    unit_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(1)],
        default=0)  # Default value set to 0
    inventory = models.IntegerField(validators=[MinValueValidator(0)], default=0)  # Default value set to 0
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
