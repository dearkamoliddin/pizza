from django.db import models


class ScrollModel(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='images/')
    discount = models.PositiveSmallIntegerField(default=0)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Discount product'
        verbose_name_plural = 'Discount products'
