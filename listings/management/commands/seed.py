from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing, Booking, Review
from decimal import Decimal
from datetime import date, timedelta
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing data before seeding',
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting database seeding...'))
        
        # Clear existing data if requested
        if options['clear']:
            self.stdout.write('Clearing existing data...')
            Review.objects.all().delete()
            Booking.objects.all().delete()
            Listing.objects.all().delete()
            User.objects.filter(is_superuser=False).delete()
        
        # Create sample users
        users_data = [
            {'username': 'alice_host', 'email': 'alice@example.com', 'first_name': 'Alice', 'last_name': 'Johnson'},
            {'username': 'bob_traveler', 'email': 'bob@example.com', 'first_name': 'Bob', 'last_name': 'Smith'},
            {'username': 'carol_explorer', 'email': 'carol@example.com', 'first_name': 'Carol', 'last_name': 'Davis'},
            {'username': 'david_host', 'email': 'david@example.com', 'first_name': 'David', 'last_name': 'Wilson'},
            {'username': 'eve_guest', 'email': 'eve@example.com', 'first_name': 'Eve', 'last_name': 'Brown'},
        ]

        users = []
        for user_data in users_data:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults={
                    'email': user_data['email'],
                    'first_name': user_data['first_name'],
                    'last_name': user_data['last_name']
                }
            )
            if created:
                user.set_password('password123')
                user.save()
                self.stdout.write(f'Created user: {user.username}')
            else:
                self.stdout.write(f'User already exists: {user.username}')
            users.append(user)

        # Sample listings data
        listings_data = [
            {
                'name': 'Cozy Beachfront Villa',
                'description': 'Beautiful villa with direct beach access and stunning ocean views. Perfect for families and couples looking for a relaxing getaway.',
                'location': 'Malibu, California',
                'pricepernight': Decimal('350.00')
            },
            {
                'name': 'Mountain Cabin Retreat',
                'description': 'Rustic cabin nestled in the mountains with hiking trails nearby. Ideal for nature lovers and adventure seekers.',
                'location': 'Aspen, Colorado',
                'pricepernight': Decimal('275.00')
            },
            {
                'name': 'Downtown Luxury Loft',
                'description': 'Modern loft in the heart of downtown with city skyline views. Walking distance to restaurants and entertainment.',
                'location': 'New York, New York',
                'pricepernight': Decimal('450.00')
            },
            {
                'name': 'Lakeside Cottage',
                'description': 'Charming cottage by the lake with private dock access. Great for fishing and water activities.',
                'location': 'Lake Tahoe, California',
                'pricepernight': Decimal('225.00')
            },
            {
                'name': 'Desert Oasis Resort',
                'description': 'Luxury resort-style home in the desert with pool facilities. Features stunning sunset views and modern amenities.',
                'location': 'Scottsdale, Arizona',
                'pricepernight': Decimal('400.00')
            }
        ]

        # Create listings
        listings = []
        for i, listing_data in enumerate(listings_data):
            listing, created = Listing.objects.get_or_create(
                name=listing_data['name'],
                defaults={
                    'host_id': users[i % 3],  # Rotate between first 3 users as hosts
                    'description': listing_data['description'],
                    'location': listing_data['location'],
                    'pricepernight': listing_data['pricepernight']
                }
            )
            listings.append(listing)
            if created:
                self.stdout.write(f'Created listing: {listing.name}')
            else:
                self.stdout.write(f'Listing already exists: {listing.name}')

        # Create sample bookings
        booking_count = 0
        for i in range(15):  # Try to create 15 bookings
            try:
                start_date = date.today() + timedelta(days=random.randint(1, 90))
                duration = random.randint(2, 7)
                end_date = start_date + timedelta(days=duration)
                listing = random.choice(listings)
                user = random.choice(users[2:])  # Last 3 users as guests
                
                total_price = listing.pricepernight * duration
                
                booking, created = Booking.objects.get_or_create(
                    property_id=listing,
                    user_id=user,
                    start_date=start_date,
                    end_date=end_date,
                    defaults={'total_price': total_price}
                )
                if created:
                    booking_count += 1
                    self.stdout.write(f'Created booking: {booking.booking_id}')
            except Exception as e:
                continue

        # Create sample reviews
        review_comments = [
            "Amazing place! The location was perfect and the host was very responsive. Highly recommend!",
            "Great location and very clean. Everything was exactly as described. Will definitely book again.",
            "Perfect for a weekend getaway. Beautiful views and all amenities were top-notch.",
            "Host was very responsive and helpful throughout our stay. The property exceeded expectations.",
            "Beautiful views and comfortable stay. Great value for money and excellent communication.",
            "Fantastic property with amazing amenities. The location couldn't be better!",
            "Clean, comfortable, and exactly as advertised. Perfect for our family vacation.",
            "Outstanding hospitality and beautiful property. Would recommend to anyone!"
        ]

        review_count = 0
        for i in range(12):  # Try to create 12 reviews
            try:
                listing = listings[i % len(listings)]
                user = users[(i + 2) % len(users)]
                
                review, created = Review.objects.get_or_create(
                    property_id=listing,
                    user_id=user,
                    defaults={
                        'rating': random.randint(4, 5),
                        'comment': review_comments[i % len(review_comments)]
                    }
                )
                if created:
                    review_count += 1
                    self.stdout.write(f'Created review: {review.review_id}')
            except Exception as e:
                continue

        self.stdout.write(
            self.style.SUCCESS(
                f'\n=== SEEDING COMPLETED ===\n'
                f' Users: {len(users)}\n'
                f' Listings: {len(listings)}\n'
                f'Bookings: {booking_count}\n'
                f'Reviews: {review_count}\n'
                f'\nDatabase successfully seeded with sample data!'
            )
        )