from django.db import models


class Item(models.Model):
    name = models.CharField(
        max_length=200,
        db_index=True,
    )
    description = models.TextField(
        blank=True,
    )
    price = models.DecimalField(
        max_digits=20,
        decimal_places=2,
    )
