from django.db import models
from rest_framework_api_key.models import APIKey
# Create your models here.
from django.db import models
from datetime import datetime

class AppSetting(models.Model):
    api_key = models.OneToOneField(APIKey, on_delete=models.CASCADE, related_name="settings")
    currency = models.CharField(max_length=10, default="USD")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.currency}'

class AddTransaction(models.Model):
    TRANSACTION_TYPES = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    )
    api_key = models.ForeignKey(APIKey, on_delete=models.CASCADE, related_name="transactions")
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    category = models.CharField(max_length=100, default='None', blank=True)
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPES, blank=True)
    date = models.DateField(default=datetime.today())
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.amount} ({self.type}) | {self.api_key}"