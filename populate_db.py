import csv, os, random, glob
from django.utils.text import slugify
from store.models import Offer, Category, Owner
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'booking_project.settings')
django.setup()


def determine_category(name):
    if 'house' in name.lower():
        return Category.objects.get_or_create(name='cottages')[0]
    elif 'apartment' in name.lower():
        return Category.objects.get_or_create(name='apartments')[0]
    elif 'bungalow' in name.lower():
        return Category.objects.get_or_create(name='bungalows')[0]
    elif 'penthouse' in name.lower():
        return Category.objects.get_or_create(name='penthouses')[0]
    elif 'tent' or 'camping' in name.lower():
        return Category.objects.get_or_create(name='campings')[0]
    elif 'room' in name.lower():
        return Category.objects.get_or_create(name='hotels')[0]
    else:
        return Category.objects.get_or_create(name='others')[0]


def generate_slug(name, owned_by_name):
    slug_text = f"{name}-{owned_by_name}"
    return slugify(slug_text)


def get_random_image():
    image_folder = '/pictures'
    images = glob.glob(os.path.join(image_folder, '*.jpg')) + glob.glob(os.path.join(image_folder, '*.png')) + glob.glob(os.path.join(image_folder, '*.jpeg')) + glob.glob(
        os.path.join(image_folder, '*.webp'))
    return random.choice(images)


def import_offers_from_csv(csv_file_path):
    with open('database/booking_hotel.csv', 'r', encoding='unicode') as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = determine_category(row['Room Type'])

            owned_by, created = Owner.objects.get_or_create(owner_name=row['Hotel Name'], location=row['Location'], slug=slugify(row['Hotel Name']))

            rating = float(row['Rating']) // 2
            slug = generate_slug(row['Room Type'], row['Hotel Name'])
            period = random.choice(['D', 'M', 'Y'])
            image_path = get_random_image()

            offer = Offer.objects.create(
                category=category,
                owned_by=owned_by,
                name=row['Room Type'],
                slug=slug,
                location=row['Location'],
                price=float(row['Room Price']),
                is_available=True,
                is_active=True,
                rating=rating,
                period = period,
                room_type = row['Bed Type'],
                picture = image_path,
            )

            offer.save()

    print('Database populated successfully')

