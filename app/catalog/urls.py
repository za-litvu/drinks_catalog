# catalog/urls.py
from django.urls import path
from .views import catalog, detail


app_name = "catalog"

urlpatterns = [
    path("", catalog.DrinkListView.as_view(), name="index"),
    path("<int:pk>/", detail.DrinkDetailView.as_view(), name="detail"),
]
