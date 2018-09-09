from django.db import models


# Create your models here.
class EmployeeInformation(models.Model):
    name = models.CharField(max_length=59)
    designation = models.CharField(max_length=150, null=True, blank=True)
    employee_id = models.IntegerField()
    department = models.CharField(max_length=50)
    team_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    address = models.TextField(null=True, blank=True)
    joining_date = models.DateField(null=True, blank=True)
    working_area = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
