from django.db import models
from moderator.models import MainUser

class Home(models.Model):
    user = models.models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name = 'Egasi')
    photo = models.ImageField(upload_to = 'images/home', vesrbose_name = 'Rasm')
    address = models.CharField(max_length = 100, verbose_name='Manzil')
    num_of_rooms = models.PozitiveSmallIntegerField()