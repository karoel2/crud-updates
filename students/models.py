from django.conf import settings
from django.db import models
from django.db.models import CharField

# Create your models here.

def upload_updated_image(instance, filename):
    return "updates/{user}/{filename}".format(user=instance.user, filename=filename)


class Update(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    content     = models.TextField(blank=True, null=True)
    image       = models.ImageField(upload_to=upload_updated_image, blank=True, null=True)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content or ""

class Student(models.Model):
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=32, null=False)
    surname     = models.CharField(max_length=32, null=False)
    dateOfBirth = models.DateField(null=False)
    login       = models.CharField(max_length=32, null=False)
    isDeleted   = models.BooleanField(default=False, null=False)

    def __str__(self):
        return f'{self.name} {self.surname}' or ""

    def detailed(self):
        return f'{self.id}    {self.name} {self.surname}       {self.dateOfBirth}  {self.login}'
    #
    def properties(self):
        return [vars(self)[item] for item in vars(self)][1::]

#
# class User(models.Model):
#     id          = models.AutoField(primary_key=True)
#     name        = models.CharField(max_length=32)
#     surname     = models.CharField(max_length=32, null=True)
#     dateOfBirth = models.DateField(null=True)
#     login       = models.CharField(max_length=32, null=True)
#     isDeleted   = models.BooleanField(default=False, null=False)
#
#     def __str__(self):
#         return f'{self.name} {self.surname}' or ""
#
#     def detailed(self):
#         return f'{self.id}    {self.name} {self.surname}       {self.dateOfBirth}  {self.login}'
#
#     def properties(self):
#         return [vars(self)[item] for item in vars(self)][1::]
