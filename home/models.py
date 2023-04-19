from django.db import models
from moderator.models import MainUser

class Home(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    price = models.PositiveIntegerField(verbose_name='Narxi')
    user  = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to = 'images/home')
    address = models.CharField(max_length = 100, verbose_name='Manzil')
    city = models.CharField(max_length=100, verbose_name='Shahar', null=True, blank=True)
    num_of_rooms = models.PositiveSmallIntegerField(verbose_name='Xonalar soni')
    area = models.SmallIntegerField(verbose_name='Uy maydoni', null=False, blank=True)
    
    def __str__(self) -> str:
        return f"{self.title}"
    
    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Home'