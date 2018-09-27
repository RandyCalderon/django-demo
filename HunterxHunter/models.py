from django.db import models
from uuid import uuid4

# Create your models here.
class Hunter(models.Model):
    id = models.UUIDField(primary_key = True, default=uuid4, editable=False)
    name = models.CharField(max_length=40)
    appearance = models.CharField(max_length=40)
    nen_type = models.CharField(max_length=20)
    background = models.TextField(blank=True)

