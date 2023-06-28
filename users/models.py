from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name= 'profile')
    phone = models.CharField(max_length=25, null= True, blank= True)
    birth_date = models.DateField(null= True, blank= True)
    company_name = models.CharField(max_length=100, null=True, blank= True)
    occupation = models.CharField(max_length=100, null=True, blank= True)
    profile_picture = models.ImageField(upload_to='profile_picture',null= True, blank= True)

    def __str__(self):
        return self.user.username
    

    
