from login.models import *
from django.db import models
<<<<<<< HEAD
from login.models import User
=======
>>>>>>> 04175478770fd5d5c89c7aab388674618ab0ab77

# Create your models here.

class Reservation(models.Model) :
    create_time = models.DateTimeField(auto_now=True)
    reservation_time = models.DateTimeField()
    people = models.IntegerField()
    
<<<<<<< HEAD
class Relate_reserv(models.Model) :
    reservate = models.ForeignKey("Reservation", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey("login.Restaurant", on_delete=models.CASCADE)
=======
class relate_reserv(models.Model) :
    reservate = models.ForeignKey("Reservation", on_delete=models.CASCADE)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    restaurant = models.ForeignKey("login.Restaurant", on_delete=models.CASCADE)
    class Meta :
        abstract = True
>>>>>>> 04175478770fd5d5c89c7aab388674618ab0ab77

class Menu(models.Model) :
    restaurant = models.ForeignKey("login.Restaurant", on_delete=models.CASCADE)
    food = models.ForeignKey("Food", on_delete=models.CASCADE)

class Food (models.Model) :
    food = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(blank=True, upload_to='food_image')