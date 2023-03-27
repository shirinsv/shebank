from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class district(models.Model):
    dist_name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=50,unique=True)
    def __str__(self):
        return self.dist_name

class dist_branch(models.Model):
    branch_name=models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    district=models.ForeignKey(district,on_delete=models.CASCADE)
    def __str__(self):
        return self.branch_name


#     logbank-userdetails
