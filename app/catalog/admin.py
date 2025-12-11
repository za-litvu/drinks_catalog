from django.contrib import admin
from .models import Drink, DrinkType, Tag, Review

admin.site.register(Drink)
admin.site.register(DrinkType)
admin.site.register(Tag)
admin.site.register(Review)
