
from rest_framework.views import APIView
from rest_framework.response import Response
from transactions.models import Transaction
from django.db.models.functions import TruncMonth, TruncDate
from django.db.models import Sum

# Category summary view

class CategorySummaryView(APIView):
    def get(self, request):
        data = (
            Transaction.objects
            .values('category')
            .annotate(total=Sum('amount'))
            .order_by('-total')
        )
        return Response(data)
    

# Daily summary view

class DailySummaryView(APIView):
    def get(self, request):
        data = (
            Transaction.objects
            .annotate(date=TruncDate('created_at'))
            .values('date')
            .annotate(total=Sum('amount'))
            .order_by('-date')
        )
        return Response(data)
    


# Monthly summary view

class MonthlySummaryView(APIView):
    def get(self, request):
        data = (
            Transaction.objects
            .annotate(month=TruncMonth('created_at'))
            .values('month')
            .annotate(total=Sum('amount'))
            .order_by('-month')
        )
        return Response(data)