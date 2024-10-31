# Generated by Django 5.1 on 2024-09-05 18:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0005_delete_classroom'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(blank=True, max_length=250)),
                ('room_code', models.IntegerField(blank=True)),
                ('educator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.educatorprofile')),
                ('student', models.ManyToManyField(blank=True, to='accounts.learnerprofile')),
            ],
        ),
    ]