from django.db import models
class EmployeeData(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    emaill=models.EmailField(max_length=100)
    salary=models.IntegerField()
    company=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    adress=models.CharField(max_length=100)
