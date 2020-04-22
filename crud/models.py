from django.db import models

class Employee(models.Model):
    eid=models.IntegerField(max_length=10)
    ename=models.CharField(max_length=100)
    eemail=models.EmailField()
    econtact=models.BigIntegerField(max_length=10)
    class Meta:
        db_table="employee"

