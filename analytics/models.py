from django.db import models



class CustomerData(models.Model):
    
    customer_Id  = models.IntegerField()
    category = models.CharField(max_length=20)
    mode_of_payments = models.CharField(max_length=25)
    amount_spent = models.FloatField()
    date = models.DateField()