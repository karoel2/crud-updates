from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Student
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, User
from django.views.decorators.http import require_http_methods
from .forms import StudentForm, CreateUserForm
from django.http import HttpResponseRedirect
import random
import datetime

def home(request):
    return render(request, 'base.html', {})#HOME.html

def show(request):
    student_list = [student.properties() for student in Student.objects.all()]
    student_list.sort(key=id)
    paginator = Paginator(student_list, 25) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    if page_number != None:
        page_obj = paginator.get_page(page_number)
        context = {
        'page_obj': page_obj
        }
    else:
        context = {}
    return render(request, 'show.html', context)


def user_form(request):
    form = StudentForm(request.POST)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success!')
            return HttpResponseRedirect('.')
    context = {
               'form': form,
               }
    return render(request, 'user_form.html', context)

def user_prolfie_list(request):#editOrDelete
    student_list = [student.properties() for student in Student.objects.all()]
    student_list.sort(key=id)
    paginator = Paginator(student_list, 25) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    if page_number != None:
        page_obj = paginator.get_page(page_number)
        context = {
        'page_obj': page_obj
        }
    else:
        context = {}
    return render(request, 'students_edit.html', context)


# @require_http_methods(["GET", "POST"])
def user_prolfie_view(request, page, student_id):#EDIT
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            edit = get_object_or_404(Student, id=student_id)
            edit.name = form.cleaned_data.get('name')
            edit.surname = form.cleaned_data.get('surname')
            edit.dateOfBirth = form.cleaned_data.get('dateOfBirth')
            edit.login = form.cleaned_data.get('login')
            edit.isDeleted = False
            edit.save()
            return redirect('home')
            # return redirect(f'../../../profile/?page={page}')
    else:
        student = get_object_or_404(Student, id=student_id)
        form = StudentForm()
        context = {'user_properties': student.properties(),
                   'form': form}
        return render(request, 'profile_view.html', context)

def user_prolfie_delete(request, page, student_id):
    edit = get_object_or_404(Student, id=student_id)
    edit.isDeleted = True
    edit.save()
    return redirect(f'../../../profile/?page={page}')#user_prolfie_list(request)

def restart(request):
    def random_date():
        start_date = datetime.date(1970, 1, 1)
        end_date = datetime.date(2000, 2, 1)

        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)

        return random_date
    Student.objects.all().delete()
    surnames = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin', 'Lee', 'Perez', 'Thompson', 'White', 'Harris', 'Sanchez']
    names = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer', 'Michael', 'Linda', 'William', 'Elizabeth', 'David', 'Barbara', 'Richard', 'Susan', 'Joseph', 'Jessica', 'Thomas', 'Sarah', 'Charles', 'Karen', 'Christopher', 'Nancy', 'Daniel', 'Lisa', 'Matthew', 'Margaret']
    for _ in range(200):
        name = random.choice(names)
        surname = random.choice(surnames)
        login = name[:3] + surname[:3] + str(random.randrange(999)+1)
        date = random_date()
        Student.objects.create(name=name,
                               surname=surname,
                               dateOfBirth=date,
                               login=login,
                               )
    return redirect('home')


def reditect_to_home(request):
    return redirect('..')

def login_v(request):
    logout(request)
    return render(request, 'login.html', context)

def logout_v(request):
    context = {}
    return redirect('..')

def register_v(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            print("\n\nOK\n\n")
            print(*form,sep='\n')
            # username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            raw_password2 = form.cleaned_data.get('password2')
            if raw_password and raw_password2:
                if raw_password == raw_password2:
                    form.save()
                    print('\n',email,raw_password, raw_password2)
                    account = authenticate(email=email, raw_password=raw_password)
                    print(account)
                    if account is not None:
                        login(request, account)
                else:
                    print("\n\nERROR\n\n")
                    raise forms.ValidationError(_(u"Passwords didn't match."))
            else:
                print("\n\nERROR\n\n")
                raise forms.ValidationError(_(u"Passwords can't be blank."))
        else:
            print("\n\nNOT\n\n")
            print(*form,sep='\n')
    context = {'form': form}
    return render(request, 'register.html', context)
