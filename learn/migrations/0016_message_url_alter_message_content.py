# Generated by Django 5.1 on 2024-09-15 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0015_alter_personalmessage_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
