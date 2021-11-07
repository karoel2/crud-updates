from django import forms
from django.forms import CharField, Textarea, DateField
import datetime

class DateInput(forms.DateInput):
    input_type = 'date'


class UserForm(forms.Form):
    name        = CharField(label="name", max_length=32)
    surname     = CharField(label="surname", max_length=32)
    dateOfBirth  = forms.DateField(widget=DateInput) #label='What is your birth date?', widget=forms.SelectDateWidget)
    login       = CharField(label="login", max_length=32)

from django.forms import ModelForm
from django.contrib.auth.forms import User, UserCreationForm
# from django.contrib.auth.forms import
from django import forms
# from django.db.models import CharField
from students.models import Student


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'dateOfBirth', 'login']
