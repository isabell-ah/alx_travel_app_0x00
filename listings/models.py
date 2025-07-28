from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid

class Listing(models.Model):
    listing_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    host_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    pricepernight = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    property_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bookings')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(end_date__gt=models.F('start_date')),
                name='end_date_after_start_date'
            )
        ]

    def __str__(self):
        return f"Booking {self.booking_id}"

class Review(models.Model):
    review_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    property_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reviews')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('property_id', 'user_id')

    def __str__(self):
        return f"Review by {self.user_id.username} - {self.rating} stars"
