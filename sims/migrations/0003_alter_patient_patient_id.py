# Generated by Django 3.2.25 on 2024-04-12 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sims', '0002_alter_patient_patient_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='Patient_Id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
