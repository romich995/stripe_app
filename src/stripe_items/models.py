from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.50'))])

    def __str__(self):
        return f"Item(id={self.id}, name='{self.name}', ...)"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
        }