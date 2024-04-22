# Generated by Django 4.0 on 2024-04-22 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150, unique=True)),
                ('short_name', models.CharField(max_length=10, unique=True)),
                ('code', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
