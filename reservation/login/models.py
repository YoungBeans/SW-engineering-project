from django.db import models
# Create your models here.

class NormalUser(models.Model) :
    idName = models.CharField(max_length=10)
    password = models.CharField(max_length=16)
    nickName = models.CharField(max_length=10)

    point = models.IntegerField(default = 0) # 수정 후 부분

    # str로 변경 
    def __str__(self) :
        return self.nickName

class User(NormalUser) :
    phoneNumber = models.CharField(max_length=12)

    reservCount = models.IntegerField(default = 0)
    # point = models.IntegerField(default = 0)
    isManager = models.BooleanField(default=False)
    isVip = models.BooleanField(default=False)
    isBlack = models.BooleanField(default=False)
    

    isManager = models.BooleanField(default=False)



class Point_relate(models.Model) :
    point = models.IntegerField()

class Location(models.Model) :
    city = models.CharField(max_length=30)
    # str로 변경 
    def __str__(self) :
        return self.city

class Restaurant(models.Model) :
    name = models.CharField(max_length=30)
    location = models.ForeignKey("Location", on_delete=models.CASCADE)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    max_customer = models.IntegerField(blank=True, null=True)
    current_customer = models.IntegerField(default=0)

class Review(models.Model) :
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField()
    menu = models.ForeignKey("reserv.Menu", on_delete=models.CASCADE, blank=True, null=True)
    star = models.IntegerField(default=0)