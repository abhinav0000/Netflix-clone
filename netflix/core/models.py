from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

AGE_CHOICES = (
    ('ALL','ALL'),
    ('Kids','Kids');

)
class CustomUser(AbstractUser):
    profiles = models.ManyToManyFiels('Profile',null=True,blank =True)

class Profile(models.Model):
    nume=models.CharField(max_length = 225)
    age_limit = models.CharField(max_length =10,choices = AGE_CHOICES)
    uuid = models.UUIDField(default=uuid.uuid4 )
