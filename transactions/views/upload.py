# transactions/views.py

import pandas as pd
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from transactions.models import Transaction
from transactions.serializers import UploadCSVSerializer
from transactions.ai_service import categorize_transaction


class UploadCSVView(GenericAPIView):
    serializer_class = UploadCSVSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        return Response({
            "message": "Use POST method to upload CSV file"
        })

    def post(self, request):
        # ✅ Step 1: Validate file
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        file = serializer.validated_data['file']

        # ✅ Step 2: Read CSV
        try:
            df = pd.read_csv(file)
        except Exception:
            return Response({"error": "Invalid CSV file"}, status=400)

        # ✅ Step 3: Validate columns
        required_columns = ['description', 'amount']
        for col in required_columns:
            if col not in df.columns:
                return Response(
                    {"error": f"Missing column: {col}"},
                    status=400
                )

        # ✅ Step 4: Convert to model objects
        transactions = []

        for _, row in df.iterrows():
            try:
                transactions.append(
                    Transaction(
                        description=str(row['description']),
                        amount=float(row['amount'])
                    )
                )
            except Exception:
                continue

        if not transactions:
            return Response({"error": "No valid data found"}, status=400)

        # ✅ Step 5: Bulk insert
        Transaction.objects.bulk_create(transactions)

        # ✅ Step 6: AI categorization (optimized)
        uncategorized = list(
            Transaction.objects.filter(category__isnull=True)
        )

        for txn in uncategorized:
            txn.category = categorize_transaction(txn.description)

        # 🚀 Bulk update instead of saving one by one
        Transaction.objects.bulk_update(uncategorized, ['category'])

        # ✅ Step 7: Response
        return Response({
            "message": "Uploaded and categorized successfully",
            "records_processed": len(transactions)
        })