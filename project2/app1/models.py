from typing import Any
from django.db import models

# Create your models here.
class product_category(models.Model):
    PCID=models.IntegerField()
    PCNAME=models.CharField(max_length=20,primary_key=True)

    def __str__(self):
        return self.PCNAME

class product(models.Model):
    PCNAME=models.ForeignKey(product_category,on_delete=models.CASCADE)
    PID=models.IntegerField()
    PNAME=models.CharField(max_length=30)
    PPRICE=models.IntegerField()
    PDATE=models.DateField()


