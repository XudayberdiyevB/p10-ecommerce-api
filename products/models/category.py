from django.core.exceptions import ValidationError
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    position = models.PositiveSmallIntegerField(default=1)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="children", null=True, blank=True)

    def __str__(self):
        return self.title

    def clean(self):
        if self.id == self.parent_id:
            raise ValidationError("Category parent id must be different")
        return super().clean()
