# Generated by Django 4.2.3 on 2024-03-24 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='Subject',
        ),
    ]
