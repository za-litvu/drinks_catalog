from django.views.generic import ListView
from django.db.models import Avg, Q
from ..models import Drink

class DrinkListView(ListView):
    model = Drink
    template_name = "index.html"
    context_object_name = "drinks"

    def get_queryset(self):
        qs = (
            Drink.objects
            .select_related("type")
            .prefetch_related("reviews")
            .annotate(avg_rating=Avg("reviews__rating"))
            .order_by("name")
        )

        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(
                Q(name__icontains=q) |
                Q(brand__icontains=q) |
                Q(tags__name__icontains=q)
            ).distinct()

        return qs
