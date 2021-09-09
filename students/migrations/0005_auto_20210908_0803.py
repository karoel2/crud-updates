# Generated by Django 3.2.6 on 2021-09-08 08:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dateOfBirth',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='login',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='student',
            name='surname',
            field=models.CharField(max_length=32),
        ),
    ]
