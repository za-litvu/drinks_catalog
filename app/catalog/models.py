from django.db import models
from PIL import Image
import os
from django.contrib.auth import get_user_model


User = get_user_model()


class DrinkType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200, blank=True, null=True)
    type = models.ForeignKey(DrinkType, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="drinks/", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="drinks/thumbs/", editable=False, null=True)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img_path = self.image.path
            thumb_path = os.path.join(
                os.path.dirname(img_path),
                "thumb_" + os.path.basename(img_path)
            )

            with Image.open(img_path) as img:
                img.thumbnail((300, 200))  # нужные размеры
                img.save(thumb_path)

            self.thumbnail.name = "drinks/" + "thumb_" + os.path.basename(img_path)
            super().save(update_fields=["thumbnail"])

    def __str__(self):
        return self.name


class Review(models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user} → {self.drink} ({self.rating})"
