from django.db import models
from moderator.models import MainUser

class Home(models.Model):
    user = models.ForeginKey(MainUser,)
    photo = models.ImageField()