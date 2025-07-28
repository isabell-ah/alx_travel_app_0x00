from rest_framework import serializers
from .models import Listing, Booking, Review

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = [
            'listing_id', 
            'host_id', 
            'name', 
            'description', 
            'location', 
            'pricepernight', 
            'created_at', 
            'updated_at'
        ]
        read_only_fields = ['listing_id', 'created_at', 'updated_at']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'booking_id',
            'property_id',
            'user_id',
            'start_date',
            'end_date',
            'total_price',
            'created_at'
        ]
        read_only_fields = ['booking_id', 'created_at']

    def validate(self, data):
        if data['end_date'] <= data['start_date']:
            raise serializers.ValidationError("End date must be after start date.")
        return data

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'review_id',
            'property_id',
            'user_id',
            'rating',
            'comment',
            'created_at'
        ]
        read_only_fields = ['review_id', 'created_at']

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value
