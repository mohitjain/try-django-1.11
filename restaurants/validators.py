from django.core.exceptions import ValidationError
CATEGORIES = [
    'Mexican',
    'Asian',
    'American',
    'Whatever'
]

def validate_category(value):
    if not value in CATEGORIES:
        raise ValidationError("This is not a valid category")
