from home.models import home
from django import forms

class HomeCreateForm(forms.ModelForm):
	class Meta:
		model = Home 
		fields = ['title',  'price', 'photo', 'address', 'city', 'num_of_rooms', 'area']