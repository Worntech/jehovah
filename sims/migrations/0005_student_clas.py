# Generated by Django 3.2.25 on 2024-04-24 08:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sims', '0004_auto_20240424_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Clas',
            field=models.CharField(choices=[('PRE', 'PRE'), ('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV'), ('V', 'V'), ('VI', 'VI'), ('VII', 'VII')], default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
    ]