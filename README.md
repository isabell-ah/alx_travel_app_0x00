# ALX Travel App 0x00

A Django-based travel application for managing property listings, bookings, and reviews.

## Project Overview

This is the foundational implementation (0x00) focusing on database modeling, serialization, and data seeding for the ALX Travel App.

## Project Structure

```
alx_travel_app_0x00/
├── alx_travel_app/                     # Django project directory
│   ├── __init__.py
│   ├── settings.py                     # Django settings configuration
│   ├── urls.py                         # Main URL routing
│   ├── wsgi.py                         # WSGI application
│   └── asgi.py                         # ASGI application
├── listings/                           # Main Django app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py                       # Database models (Listing, Booking, Review)
│   ├── serializers.py                  # API serializers (Listing, Booking, Review)
│   ├── views.py
│   ├── tests.py
│   ├── migrations/                     # Database migrations
│   └── management/                     # Management commands
│       ├── __init__.py
│       └── commands/
│           ├── __init__.py
│           └── seed.py                 # Database seeder command
├── manage.py                           # Django management script
├── README.md                           # Project documentation
└── requirements.txt                    # Python dependencies
```

## Database Models

### Listing Model

- `listing_id`: UUID primary key (auto-generated)
- `host_id`: Foreign key to Django User model
- `name`: Property name (CharField, max 200 characters)
- `description`: Detailed property description (TextField)
- `location`: Property location (CharField, max 200 characters)
- `pricepernight`: Price per night (DecimalField, 10 digits, 2 decimal places)
- `created_at`: Auto-generated creation timestamp
- `updated_at`: Auto-updated modification timestamp

### Booking Model

- `booking_id`: UUID primary key (auto-generated)
- `property_id`: Foreign key to Listing model
- `user_id`: Foreign key to Django User model
- `start_date`: Booking start date (DateField)
- `end_date`: Booking end date (DateField)
- `total_price`: Total booking cost (DecimalField)
- `created_at`: Auto-generated creation timestamp
- **Constraint**: `end_date` must be after `start_date`

### Review Model

- `review_id`: UUID primary key (auto-generated)
- `property_id`: Foreign key to Listing model
- `user_id`: Foreign key to Django User model
- `rating`: Rating from 1-5 (IntegerField with validators)
- `comment`: Review text (TextField)
- `created_at`: Auto-generated creation timestamp
- **Constraint**: Unique combination of `property_id` and `user_id`

## API Serializers

### ListingSerializer

- Handles serialization/deserialization of Listing model
- Read-only fields: `listing_id`, `created_at`, `updated_at`
- All other fields are editable

### BookingSerializer

- Handles serialization/deserialization of Booking model
- Read-only fields: `booking_id`, `created_at`
- Custom validation: ensures `end_date` is after `start_date`

### ReviewSerializer

- Handles serialization/deserialization of Review model
- Read-only fields: `review_id`, `created_at`
- Custom validation: ensures rating is between 1-5

## Setup Instructions

### 1. Environment Setup

```bash
# Clone the repository
git clone <repository-url> alx_travel_app_0x00
cd alx_travel_app_0x00

# Install dependencies
pip install django djangorestframework python-decouple
```

### 2. Database Setup

```bash
# Create and apply migrations
python manage.py makemigrations
python manage.py migrate
```

### 3. Seed Database with Sample Data

```bash
# Seed with sample data
python manage.py seed

# Or clear existing data and seed fresh
python manage.py seed --clear
```

## Database Seeding Details

The `python manage.py seed` command creates:

### Sample Users (5 total)

- `alice_host` - Host user
- `bob_traveler` - Guest user
- `carol_explorer` - Guest user
- `david_host` - Host user
- `eve_guest` - Guest user

### Sample Listings (5 total)

- Cozy Beachfront Villa (Malibu, CA) - $350/night
- Mountain Cabin Retreat (Aspen, CO) - $275/night
- Downtown Luxury Loft (New York, NY) - $450/night
- Lakeside Cottage (Lake Tahoe, CA) - $225/night
- Desert Oasis Resort (Scottsdale, AZ) - $400/night

### Sample Bookings

- Up to 15 bookings with realistic future dates
- Random durations between 2-7 days
- Calculated total prices based on duration

### Sample Reviews

- Up to 12 reviews with 4-5 star ratings
- Realistic review comments
- Unique user-property combinations

## Testing the Implementation

### Verify Database Seeding

```bash
python manage.py shell
```

```python
from listings.models import Listing, Booking, Review
from django.contrib.auth.models import User

# Check data counts
print(f"Users: {User.objects.count()}")
print(f"Listings: {Listing.objects.count()}")
print(f"Bookings: {Booking.objects.count()}")
print(f"Reviews: {Review.objects.count()}")

# Sample data inspection
print("\nSample Listings:")
for listing in Listing.objects.all()[:3]:
    print(f"- {listing.name} in {listing.location} (${listing.pricepernight}/night)")

print("\nSample Bookings:")
for booking in Booking.objects.all()[:3]:
    print(f"- {booking.property_id.name}: {booking.start_date} to {booking.end_date}")
```

### Test Serializers

```python
from listings.serializers import ListingSerializer, BookingSerializer, ReviewSerializer
from listings.models import Listing

# Test listing serialization
listing = Listing.objects.first()
serializer = ListingSerializer(listing)
print(serializer.data)
```

## Key Features Implemented

- **Database Models**: Complete models with relationships and constraints
- **API Serializers**: Full serialization support for all models
- **Data Validation**: Custom validators and constraints
- **Management Commands**: Robust database seeding functionality
- **Sample Data**: Realistic test data for development
- **Documentation**: Comprehensive project documentation

## Repository Information

- **GitHub Repository**: `alx_travel_app_0x00`
- **Main Directory**: `alx_travel_app`
- **Required Files Implemented**:
  - `listings/models.py`
  - `listings/serializers.py`
  - `listings/management/commands/seed.py`
  - `README.md`

## Next Steps

This 0x00 implementation provides the foundation for:

- API endpoints development
- User authentication system
- Frontend integration
- Advanced booking logic
- Payment processing
- Search and filtering capabilities

---

**Note**: This is the foundational phase (0x00) of the ALX Travel App project, focusing on core database modeling and data management capabilities.

### ListingSerializer

- Handles serialization/deserialization of Listing model
- Read-only fields: `listing_id`, `created_at`, `updated_at`
- All other fields are editable

### BookingSerializer

- Handles serialization/deserialization of Booking model
- Read-only fields: `booking_id`, `created_at`
- Custom validation: ensures `end_date` is after `start_date`

### ReviewSerializer

- Handles serialization/deserialization of Review model
- Read-only fields: `review_id`, `created_at`
- Custom validation: ensures rating is between 1-5

## Setup Instructions

### 1. Environment Setup

```bash
# Clone the repository
git clone <repository-url> alx_travel_app_0x00
cd alx_travel_app_0x00

# Install dependencies
pip install django djangorestframework python-decouple
```

### 2. Database Setup

```bash
# Create and apply migrations
python manage.py makemigrations
python manage.py migrate
```

### 3. Seed Database with Sample Data

```bash
# Seed with sample data
python manage.py seed

# Or clear existing data and seed fresh
python manage.py seed --clear
```

## Database Seeding Details

The `python manage.py seed` command creates:

### Sample Users (5 total)

- `alice_host` - Host user
- `bob_traveler` - Guest user
- `carol_explorer` - Guest user
- `david_host` - Host user
- `eve_guest` - Guest user

### Sample Listings (5 total)

- Cozy Beachfront Villa (Malibu, CA) - $350/night
- Mountain Cabin Retreat (Aspen, CO) - $275/night
- Downtown Luxury Loft (New York, NY) - $450/night
- Lakeside Cottage (Lake Tahoe, CA) - $225/night
- Desert Oasis Resort (Scottsdale, AZ) - $400/night

### Sample Bookings

- Up to 15 bookings with realistic future dates
- Random durations between 2-7 days
- Calculated total prices based on duration

### Sample Reviews

- Up to 12 reviews with 4-5 star ratings
- Realistic review comments
- Unique user-property combinations

## Testing the Implementation

### Verify Database Seeding

```bash
python manage.py shell
```

```python
from listings.models import Listing, Booking, Review
from django.contrib.auth.models import User

# Check data counts
print(f"Users: {User.objects.count()}")
print(f"Listings: {Listing.objects.count()}")
print(f"Bookings: {Booking.objects.count()}")
print(f"Reviews: {Review.objects.count()}")

# Sample data inspection
print("\nSample Listings:")
for listing in Listing.objects.all()[:3]:
    print(f"- {listing.name} in {listing.location} (${listing.pricepernight}/night)")

print("\nSample Bookings:")
for booking in Booking.objects.all()[:3]:
    print(f"- {booking.property_id.name}: {booking.start_date} to {booking.end_date}")
```

### Test Serializers

```python
from listings.serializers import ListingSerializer, BookingSerializer, ReviewSerializer
from listings.models import Listing

# Test listing serialization
listing = Listing.objects.first()
serializer = ListingSerializer(listing)
print(serializer.data)
```

## Key Features Implemented

- ✅ **Database Models**: Complete models with relationships and constraints
- ✅ **API Serializers**: Full serialization support for all models
- ✅ **Data Validation**: Custom validators and constraints
- ✅ **Management Commands**: Robust database seeding functionality
- ✅ **Sample Data**: Realistic test data for development
- ✅ **Documentation**: Comprehensive project documentation

## Repository Information

- **GitHub Repository**: `alx_travel_app_0x00`
- **Main Directory**: `alx_travel_app`
- **Required Files Implemented**:
  - ✅ `listings/models.py`
  - ✅ `listings/serializers.py`
  - ✅ `listings/management/commands/seed.py`
  - ✅ `README.md`

## Next Steps

This 0x00 implementation provides the foundation for:

- API endpoints development
- User authentication system
- Frontend integration
- Advanced booking logic
- Payment processing
- Search and filtering capabilities

---

**Note**: This is the foundational phase (0x00) of the ALX Travel App project, focusing on core database modeling and data management capabilities.
# alx_travel_app_0x00
