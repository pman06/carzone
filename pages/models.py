from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    faceboo_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    google_plus_link = models.URLField(max_length=100)
    created_date = models.DateTimeField(auto_now_add =True)

    def __str__(self):
        return self.first_name+ " "+self.last_name


class BusinessInfo(models.Model):
    business_name = models.CharField(max_length=255)
    address =  models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country =models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    email = models.EmailField()
    facebook_link = models.URLField()
    twitter_link = models.URLField()
    google_link = models.URLField()
    

    def __str__(self):
        return self.business_name
