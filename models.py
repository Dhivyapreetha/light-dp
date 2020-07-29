from django.db import models

# Create your models here.

class user(models,Models):
user_name=models.CharField(max_length=50)
mobile_no=models.IntegerField(max_length=10)
email_id=models.CharField(max_length=20)
password=models.CharField(maxlength=20)

def _str_(self):
 return self.name

