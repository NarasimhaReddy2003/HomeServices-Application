# Generated by Django 5.1 on 2024-08-17 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TechnicianModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=100)),
                ('contact', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('techrole', models.CharField(max_length=100)),
                ('profile', models.FileField(upload_to='static\\Techprofiles')),
                ('status', models.CharField(default='pending', max_length=100)),
            ],
            options={
                'db_table': 'TechnicianModel',
            },
        ),
        migrations.CreateModel(
            name='UsersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=100)),
                ('contact', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('profile', models.FileField(upload_to='static\\userprofiles')),
            ],
            options={
                'db_table': 'UsersModel',
            },
        ),
    ]
