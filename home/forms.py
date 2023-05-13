from home.models import Home
from django import forms

class HomeCreateForm(forms.ModelForm):
	class Meta:
		model = Home 
		fields = ['title',  'price', 'photo', 'address', 'city', 'num_of_rooms', 'area']

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
class HomeFilterForm(forms.Form):
    city = forms.ChoiceField(choices=Home.UZBEKISTAN_REGION_CHOICES)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].widget.attrs.update({'class': 'form-control'})

class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = ['title', 'price',  'photo', 'address', 'city', 'num_of_rooms', 'area', 'description']
        widgets = {'description': forms.Textarea(attrs={'cols': 80, 'rows': 5})}

