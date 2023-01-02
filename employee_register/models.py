from django.db import models

class Position(models.Model):
    title = models.CharField(max_length=50)
    job_description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.title

class Employee(models.Model):
    family_name = models.CharField(max_length=50)
    given_name = models.CharField(max_length=100)
    preferred_name = models.CharField(null=True, blank=True, max_length=100)
    emp_code = models.CharField(max_length=6)
    mobile_no = models.CharField(max_length=15)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.preferred_name
    