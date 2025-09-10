from django.db import models
from django.utils import timezone
from django.contrib.postgres.indexes import HashIndex, BrinIndex


class Contact(models.Model):
    phone = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.phone


class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    about = models.CharField(max_length=10000)
    age = models.SmallIntegerField(null=True)
    created = models.DateTimeField(default=timezone.now, null=True)
    work_experience = models.SmallIntegerField(default=0, null=True)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

    class Meta:
        indexes = (
            HashIndex(
                fields=('about',),
                name="hr_%(class)s_about_ix",
            ),
            BrinIndex(
                fields=('created',), name="hr_employee_created_ix",
                pages_per_range=2
            )
        )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'