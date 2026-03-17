# transactions/views.py

import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Transaction
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import UploadCSVSerializer
from .ai_service import categorize_transaction

class UploadCSVView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        return Response({
            "message": "Use POST method to upload CSV file"
        })

    def post(self, request):
        serializer = UploadCSVSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        file = serializer.validated_data['file']

        df = pd.read_csv(file)

        transactions = []

        for _, row in df.iterrows():
            transactions.append(
                Transaction(
                    description=row['description'],
                    amount=row['amount']
                )
            )

    
        # Save all
        Transaction.objects.bulk_create(transactions)

        # 🔥 NOW RUN AI
        uncategorized = Transaction.objects.filter(category__isnull=True)

        for txn in uncategorized:
            txn.category = categorize_transaction(txn.description)
            txn.save()

        return Response({"message": "Uploaded successfully"})