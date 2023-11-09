from django.db import models

class Car(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()
    model = models.CharField(max_length=100)
    # Boshqa hususiyatlar uchun kerakli maydonlar