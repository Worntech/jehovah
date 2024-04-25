# Generated by Django 3.2.25 on 2024-04-24 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sims', '0003_alter_patient_patient_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100)),
                ('Middle_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Year', models.CharField(choices=[('2024', '2024'), ('2025', '2025'), ('2026', '2026'), ('2027', '2027'), ('2028', '2028'), ('2029', '2029'), ('2030', '2030'), ('2031', '2031')], max_length=40)),
                ('Clas', models.CharField(choices=[('PRE', 'PRE'), ('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV'), ('V', 'V'), ('VI', 'VI'), ('VII', 'VII')], max_length=40)),
                ('Payed', models.IntegerField()),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100)),
                ('Middle_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Year', models.CharField(choices=[('2024', '2024'), ('2025', '2025'), ('2026', '2026'), ('2027', '2027'), ('2028', '2028'), ('2029', '2029'), ('2030', '2030'), ('2031', '2031')], max_length=40)),
                ('Clas', models.CharField(choices=[('PRE', 'PRE'), ('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV'), ('V', 'V'), ('VI', 'VI'), ('VII', 'VII')], max_length=40)),
                ('Semister', models.CharField(choices=[('I', 'I'), ('II', 'II')], max_length=40)),
                ('Mathematic', models.IntegerField()),
                ('English', models.IntegerField()),
                ('Kiswahili', models.IntegerField()),
                ('History', models.IntegerField()),
                ('Geograph', models.IntegerField()),
                ('Sayansi', models.IntegerField()),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100)),
                ('Middle_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=40)),
                ('Age', models.CharField(max_length=100)),
                ('Parent_Name', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=100)),
                ('Parent_Place', models.CharField(max_length=100)),
                ('Year', models.CharField(choices=[('2024', '2024'), ('2025', '2025'), ('2026', '2026'), ('2027', '2027'), ('2028', '2028'), ('2029', '2029'), ('2030', '2030'), ('2031', '2031')], max_length=40)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
            ],
        ),
        migrations.RemoveField(
            model_name='acr',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='acr',
            name='user',
        ),
        migrations.RemoveField(
            model_name='clinics',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='clinics',
            name='user',
        ),
        migrations.RemoveField(
            model_name='conjunctival',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='conjunctival',
            name='user',
        ),
        migrations.RemoveField(
            model_name='conjunctivar',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='conjunctivar',
            name='user',
        ),
        migrations.RemoveField(
            model_name='corneal',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='corneal',
            name='user',
        ),
        migrations.RemoveField(
            model_name='cornear',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='cornear',
            name='user',
        ),
        migrations.RemoveField(
            model_name='diagnosis',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='diagnosis',
            name='user',
        ),
        migrations.RemoveField(
            model_name='eyelidl',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='eyelidl',
            name='user',
        ),
        migrations.RemoveField(
            model_name='eyelidr',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='eyelidr',
            name='user',
        ),
        migrations.RemoveField(
            model_name='family',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='family',
            name='user',
        ),
        migrations.RemoveField(
            model_name='general',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='general',
            name='user',
        ),
        migrations.RemoveField(
            model_name='history',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='history',
            name='user',
        ),
        migrations.RemoveField(
            model_name='investigation',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='investigation',
            name='user',
        ),
        migrations.RemoveField(
            model_name='iopa',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='iopa',
            name='user',
        ),
        migrations.RemoveField(
            model_name='iopb',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='iopb',
            name='user',
        ),
        migrations.RemoveField(
            model_name='irisl',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='irisl',
            name='user',
        ),
        migrations.RemoveField(
            model_name='irisr',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='irisr',
            name='user',
        ),
        migrations.RemoveField(
            model_name='le',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='le',
            name='user',
        ),
        migrations.RemoveField(
            model_name='lensl',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='lensl',
            name='user',
        ),
        migrations.RemoveField(
            model_name='lensr',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='lensr',
            name='user',
        ),
        migrations.RemoveField(
            model_name='management',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='management',
            name='user',
        ),
        migrations.RemoveField(
            model_name='medication',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='medication',
            name='user',
        ),
        migrations.RemoveField(
            model_name='od',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='od',
            name='user',
        ),
        migrations.RemoveField(
            model_name='os',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='os',
            name='user',
        ),
        migrations.RemoveField(
            model_name='patientinfo',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='patientinfo',
            name='user',
        ),
        migrations.RemoveField(
            model_name='pupill',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='pupill',
            name='user',
        ),
        migrations.RemoveField(
            model_name='pupilr',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='pupilr',
            name='user',
        ),
        migrations.RemoveField(
            model_name='re',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='re',
            name='user',
        ),
        migrations.RemoveField(
            model_name='retinal',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='retinal',
            name='user',
        ),
        migrations.RemoveField(
            model_name='retinar',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='retinar',
            name='user',
        ),
        migrations.RemoveField(
            model_name='visual',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='visual',
            name='user',
        ),
        migrations.RemoveField(
            model_name='vitreousl',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='vitreousl',
            name='user',
        ),
        migrations.RemoveField(
            model_name='vitreousr',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='vitreousr',
            name='user',
        ),
        migrations.DeleteModel(
            name='ACL',
        ),
        migrations.DeleteModel(
            name='ACR',
        ),
        migrations.DeleteModel(
            name='Clinics',
        ),
        migrations.DeleteModel(
            name='CONJUNCTIVAL',
        ),
        migrations.DeleteModel(
            name='CONJUNCTIVAR',
        ),
        migrations.DeleteModel(
            name='CORNEAL',
        ),
        migrations.DeleteModel(
            name='CORNEAR',
        ),
        migrations.DeleteModel(
            name='Diagnosis',
        ),
        migrations.DeleteModel(
            name='EYELIDL',
        ),
        migrations.DeleteModel(
            name='EYELIDR',
        ),
        migrations.DeleteModel(
            name='Family',
        ),
        migrations.DeleteModel(
            name='General',
        ),
        migrations.DeleteModel(
            name='History',
        ),
        migrations.DeleteModel(
            name='Investigation',
        ),
        migrations.DeleteModel(
            name='IOPA',
        ),
        migrations.DeleteModel(
            name='IOPB',
        ),
        migrations.DeleteModel(
            name='IRISL',
        ),
        migrations.DeleteModel(
            name='IRISR',
        ),
        migrations.DeleteModel(
            name='LE',
        ),
        migrations.DeleteModel(
            name='LENSL',
        ),
        migrations.DeleteModel(
            name='LENSR',
        ),
        migrations.DeleteModel(
            name='Management',
        ),
        migrations.DeleteModel(
            name='Medication',
        ),
        migrations.DeleteModel(
            name='OD',
        ),
        migrations.DeleteModel(
            name='OS',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
        migrations.DeleteModel(
            name='Patientinfo',
        ),
        migrations.DeleteModel(
            name='PUPILL',
        ),
        migrations.DeleteModel(
            name='PUPILR',
        ),
        migrations.DeleteModel(
            name='RE',
        ),
        migrations.DeleteModel(
            name='RETINAL',
        ),
        migrations.DeleteModel(
            name='RETINAR',
        ),
        migrations.DeleteModel(
            name='Visual',
        ),
        migrations.DeleteModel(
            name='VITREOUSL',
        ),
        migrations.DeleteModel(
            name='VITREOUSR',
        ),
    ]