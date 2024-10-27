from django.db import models

# Create your models here.

def validate_phone(value:str):
    if len(value) != 10 and int(value):
        raise ValueError("phone number must be 10 digits")
    

class Profile(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=10, validators=[validate_phone])
    profile_pic = models.ImageField(upload_to='media/profile_pics/', null=True, blank=True)


    def __str__(self):
        return f"{self.username} - Profile"