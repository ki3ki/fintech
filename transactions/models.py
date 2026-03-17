
# transactions/models.py

from django.db import models

class Transaction(models.Model):
    description = models.CharField(max_length=255)
    amount = models.FloatField()
    category = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)