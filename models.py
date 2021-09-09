from django.conf import settings
from django.db import models

class Student(models.Model):
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=32)
    surname     = models.CharField(max_length=32, null=True)
    dateOfBirth = models.DateField(null=True)
    login       = models.CharField(max_length=32, null=True)
    isDeleted   = models.BooleanField(default=False, null=False)

    def __str__(self):
        return f'{self.name} {self.surname}' or ""

    def detailed(self):
        return f'{self.id}    {self.name} {self.surname}       {self.dateOfBirth}  {self.login}'
    #
    # def properties(self):
    #     return [vars(self)[item] for item in vars(self)][1::]
