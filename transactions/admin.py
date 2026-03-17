
# transactions/admin.py

from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['description', 'amount', 'category', 'created_at']
    search_fields = ['description']
    list_filter = ['category']