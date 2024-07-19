from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=50,unique=True)
    profile_picture = models.ImageField(upload_to='account/image',blank=True,null=True)
    phone_number = models.CharField(max_length=25)
    professional_page = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"

    REQUIRED_FIELDS = ["username","first_name","last_name"]

    def clean(self):
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()
        self.email = self.email.lower()
        self.username = self.username.lower()


    def __str__(self):
        return self.email



    