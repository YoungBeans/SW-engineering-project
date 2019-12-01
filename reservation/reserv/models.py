from login.models import *
from django.db import models
from login.models import User
import random
import string
# Create your models here.

class Reservation(models.Model) :
    create_time = models.DateTimeField(auto_now=True)
    reservation_time = models.DateTimeField()
    people = models.IntegerField()
    
class Relate_reserv(models.Model) :
    reservate = models.ForeignKey("Reservation", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    restaurant = models.ForeignKey("login.Restaurant", on_delete=models.CASCADE)

class Menu(models.Model) :
    restaurant = models.ForeignKey("login.Restaurant", on_delete=models.CASCADE)
    food = models.ForeignKey("Food", on_delete=models.CASCADE)

class Food (models.Model) :
    food = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(blank=True, upload_to='food_image')

class Non_user_reservation(Reservation) :
    phone_number = models.CharField(default="None", max_length=15)
    serial_number = models.CharField(default=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8)), max_length=15)
    user_name = models.CharField(default="홍길동", max_length=20)

