from django.db import models

# Create your models here.
class user_details(models.Model):
    username=models.CharField(max_length=75)
    dob=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    phone_no=models.IntegerField()
    mail_id=models.EmailField()
    address=models.CharField(max_length=250)
    district=models.CharField(max_length=25)
    subdistrict=models.CharField(max_length=25)
    accounttype=models.CharField(max_length=30)
    material_providing=models.CharField(max_length=50)

    def __str__(self):
        return self.username

# class user_registration(models.Model):
#     username=models.CharField(max_length=150)
#     password=models.CharField(max_length=8)
#     c_password=models.CharField(max_length=8)
#
#     def __str__(self):
#         return self.username