import django_filters
from django.forms.widgets import TextInput
from django_filters import CharFilter, ChoiceFilter

from home.models import Home


UZBEKISTAN_REGION_CHOICES = [
    ('Andijan', 'Andijan'),
    ('Bukhara', 'Bukhara'),
    ('Fergana', 'Fergana'),
    ('Jizzakh', 'Jizzakh'),
    ('Khorezm', 'Khorezm'),
    ('Namangan', 'Namangan'),
    ('Navoiy', 'Navoiy'),
    ('Qashqadaryo', 'Qashqadaryo'),
    ('Samarqand', 'Samarqand'),
    ('Sirdaryo', 'Sirdaryo'),
    ('Surxondaryo', 'Surxondaryo'),
    ('Tashkent', 'Tashkent'),
    ('Xorazm', 'Xorazm'),
    ('Qoraqalpog\'iston', 'Qoraqalpog\'iston'),
]

class HomeFilter(django_filters.FilterSet):
    city = ChoiceFilter(choices=UZBEKISTAN_REGION_CHOICES)

    class Meta:
        model = Home
        fields = ['city',]