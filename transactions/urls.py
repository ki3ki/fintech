# transactions/urls.py

from django.urls import path
from .views.analytics import (
    
    CategorySummaryView,
    DailySummaryView,
    MonthlySummaryView
)
from .views.upload import UploadCSVView

urlpatterns = [
    path('upload/', UploadCSVView.as_view()),

    # Analytics
    path('analytics/category/', CategorySummaryView.as_view()),
    path('analytics/daily/', DailySummaryView.as_view()),
    path('analytics/monthly/', MonthlySummaryView.as_view()),
]