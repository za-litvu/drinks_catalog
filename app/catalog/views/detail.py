from django.views.generic import DetailView
from django.db.models import Avg
from ..models import Drink

class DrinkDetailView(DetailView):
    model = Drink
    template_name = "detail.html"
    context_object_name = "drink"
    def get_queryset(self):
        return (
            Drink.objects
            .select_related("type")
            .prefetch_related("reviews__user")
            .annotate(avg_rating=Avg("reviews__rating"))
        )