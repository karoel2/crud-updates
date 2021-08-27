from django.shortcuts import render

from .models import User

from django.contrib import messages


def home(request):
    return render(request, 'home.html', {})

def show(request):
    users = User.objects.all()
    list = []
    for it in users:
        list.append(it.properties())
    context = {
    'user_properties': list
    }
    return render(request, 'show.html', context)

from django.views.decorators.http import require_http_methods
from .forms import UserForm

@require_http_methods(["GET", "POST"])
def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            User.objects.create(name=form.cleaned_data.get('name'),
                                   surname=form.cleaned_data.get('surname'),
                                   dateOfBirth=form.cleaned_data.get('dateOfBirth'),
                                   login=form.cleaned_data.get('login'),
                                   )
            messages.success(request, 'Success!')
            return HttpResponseRedirect('.')
    else:
        form = UserForm()
    context = {'title': 'Form View',
               'form': form,
               'path': request.path,}
               # 'entries': Message.objects.all()}
    return render(request, 'user_form.html', context)


def user_prolfie_list(request):
    users = User.objects.all()
    list = []
    for it in users:
        list.append(it.properties())
    context = {
    'user_properties': list
    }
    return render(request, 'students_edit.html', context)


from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect

@require_http_methods(["GET", "POST"])
def user_prolfie_view(request, user_id):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            edit = get_object_or_404(User, id=user_id)
            edit.name=form.cleaned_data.get('name')
            edit.surname=form.cleaned_data.get('surname')
            edit.dateOfBirth=form.cleaned_data.get('dateOfBirth')
            edit.login=form.cleaned_data.get('login')
            edit.save()
            messages.success(request, 'Success!')
            return HttpResponseRedirect('.')
    else:
        user = get_object_or_404(User, id=user_id)
        context = {'user_properties': user.properties()}
        return render(request, 'profile_view.html', context)

def user_prolfie_delete(request, user_id):
    edit = get_object_or_404(User, id=user_id)
    edit.isDeleted = True
    edit.save()
    return redirect('profile')#user_prolfie_list(request)

import random
import datetime

def random_date():
    start_date = datetime.date(1970, 1, 1)
    end_date = datetime.date(2000, 2, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    return random_date

def restart(request):
    User.objects.all().delete()
    surnames = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin', 'Lee', 'Perez', 'Thompson', 'White', 'Harris', 'Sanchez']
    names = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer', 'Michael', 'Linda', 'William', 'Elizabeth', 'David', 'Barbara', 'Richard', 'Susan', 'Joseph', 'Jessica', 'Thomas', 'Sarah', 'Charles', 'Karen', 'Christopher', 'Nancy', 'Daniel', 'Lisa', 'Matthew', 'Margaret']
    for _ in names:
        name = random.choice(names)
        surname = random.choice(surnames)
        login = name[:3] + surname[:3] + str(random.randrange(999)+1)
        date = random_date()
        User.objects.create(name=name,
                               surname=surname,
                               dateOfBirth=date,
                               login=login,
                               )
    return redirect('home')

# Create your views here.
