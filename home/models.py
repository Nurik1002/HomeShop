from django.db import models
from moderator.models import MainUser

class Home(models.Model):

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
    ('Toshkent City', 'Toshkent City'),
    ('Xorazm', 'Xorazm'),]


    title = models.CharField(max_length=100, verbose_name="Title")
    price = models.PositiveIntegerField(verbose_name='Narxi')
    user  = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to = 'images/home',  default='images/home/default.png')
    address = models.CharField(max_length = 100, null=True, blank=True, verbose_name='Manzil')
    city = models.CharField(max_length=100, verbose_name='Shahar',choices = UZBEKISTAN_REGION_CHOICES, default = 'Tashkent')
    num_of_rooms = models.PositiveSmallIntegerField(verbose_name='Xonalar soni')
    area = models.SmallIntegerField(verbose_name='Uy maydoni', null=False, blank=True)
    
    def __str__(self) -> str:
        return f"{self.title}"
    
    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Home'