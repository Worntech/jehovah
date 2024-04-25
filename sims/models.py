from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.contrib import messages
import uuid

from django.contrib.auth import get_user_model


# user table--------------------------------------------------------------------
# class MyUserManager(BaseUserManager):
#     def create_user(self, email, username, first_name, password=None):
#         if not email:
#             raise ValueError("email is required")
#         if not username:
#             raise ValueError("Your user name is required")
#         if not first_name:
#             raise ValueError("Your First Name is required")
#         # if not last_name:
#         #     raise ValueError("Your Last Name is required")
#         # if not id:
#         #     raise ValueError("Your Middle Name is required")
        
        

#         user=self.model(
#             email=self.normalize_email(email),
#             username=username,
#             first_name=first_name,
#             # last_name=last_name,
#             # middle_name=middle_name,
#             # phone=phone,
#             # id=id,
#             # course=course,
            
            
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#     def create_superuser(self, email, username, password=None):
#         user=self.create_user(
#             email=self.normalize_email(email),
#             username=username,
#             password=password,
#             # first_name=first_name,
#             # last_name=last_name,

#         )
#         user.is_admin=True
#         user.is_staff=True
        
#         user.is_superuser=True
#         user.save(using=self._db)
#         return user





class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("email is required")
        if not username:
            raise ValueError("Your user name is required")
        
        

        user=self.model(
            email=self.normalize_email(email),
            username=username,
            
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,

        )
        user.is_admin=True
        user.is_staff=True
        
        user.is_superuser=True
        user.save(using=self._db)
        return user

class MyStudents(AbstractBaseUser):

    email=models.EmailField(verbose_name="email", max_length=100, unique=True)
    # first_name=models.CharField(verbose_name="first name", max_length=100, unique=False)
    username=models.CharField(verbose_name="username", max_length=100, unique=True)
    # id=models.CharField(verbose_name="id", max_length=100, unique=True, primary_key=True)
    # last_name=models.CharField(verbose_name="last name", max_length=100, unique=False)
    
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    
    last_login=models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)
    


    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['username']
    
    objects=MyUserManager()

    def __str__(self):
        return self.username

    


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

class MyStaff(AbstractBaseUser):
    email=models.EmailField(verbose_name="email", max_length=100, unique=True)
    # first_name=models.CharField(verbose_name="first name", max_length=100, unique=False)
    username=models.CharField(verbose_name="username", max_length=100, unique=True)
    # id=models.CharField(verbose_name="id", max_length=100, unique=False, primary_key=True)
    # last_name=models.CharField(verbose_name="last name", max_length=100, unique=False)
    
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    
    last_login=models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)
    


    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['username']
    
    objects=MyUserManager()

    def __str__(self):
        return self.username

    


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
class Student(models.Model):
    year = [
    ("2024", "2024"),
    ("2025", "2025"),
    ("2026", "2026"),
    ("2027", "2027"),
    ("2028", "2028"),
    ("2029", "2029"),
    ("2030", "2030"),
    ("2031", "2031"),
]
    clas = [
    ("PRE", "PRE"),
    ("I", "I"),
    ("II", "II"),
    ("III", "III"),
    ("IV", "IV"),
    ("V", "V"),
    ("VI", "VI"),
    ("VII", "VII"),
]
    sex = [
    ("Male", "Male"),
    ("Female", "Female"),
]

    First_Name = models.CharField(max_length=100)
    Middle_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Sex = models.CharField(max_length=40, choices=sex)
    Clas = models.CharField(max_length=40, choices=clas)
    Age = models.CharField(max_length=100)
    Parent_Name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=100)
    Parent_Place = models.CharField(max_length=100)
    Year = models.CharField(max_length=40, choices=year)
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    
class Result(models.Model):
    year = [
    ("2024", "2024"),
    ("2025", "2025"),
    ("2026", "2026"),
    ("2027", "2027"),
    ("2028", "2028"),
    ("2029", "2029"),
    ("2030", "2030"),
    ("2031", "2031"),
]
    awamu = [
    ("I", "I"),
    ("II", "II"),
]

    clas = [
    ("PRE", "PRE"),
    ("I", "I"),
    ("II", "II"),
    ("III", "III"),
    ("IV", "IV"),
    ("V", "V"),
    ("VI", "VI"),
    ("VII", "VII"),
]

    First_Name = models.CharField(max_length=100)
    Middle_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    
    Year = models.CharField(max_length=40, choices=year)
    Clas = models.CharField(max_length=40, choices=clas)
    Semister = models.CharField(max_length=40, choices=awamu)

    Mathematic = models.IntegerField()
    English = models.IntegerField()
    Kiswahili = models.IntegerField()
    History = models.IntegerField()
    Geograph = models.IntegerField()
    Sayansi = models.IntegerField()
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    
class Payment(models.Model):
    year = [
    ("2024", "2024"),
    ("2025", "2025"),
    ("2026", "2026"),
    ("2027", "2027"),
    ("2028", "2028"),
    ("2029", "2029"),
    ("2030", "2030"),
    ("2031", "2031"),
]
    clas = [
    ("PRE", "PRE"),
    ("I", "I"),
    ("II", "II"),
    ("III", "III"),
    ("IV", "IV"),
    ("V", "V"),
    ("VI", "VI"),
    ("VII", "VII"),
]

    First_Name = models.CharField(max_length=100)
    Middle_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    
    Year = models.CharField(max_length=40, choices=year)
    Clas = models.CharField(max_length=40, choices=clas)
    Payed = models.IntegerField()
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    
class StaffContactinfo(models.Model):
    region = [
    ("Arusha", "Arusha"),
    ("Dodoma", "Dodoma"),
    ("Mwanza", "Mwanza"),
    ("Iringa", "Iringa"),
    ("Tabora", "Tabora"),

    ("Mara", "Mara"),
    ("Kagera", "Kagera"),
    ("Simiyu", "Simiyu"),
    ("Shinyanga", "Shinyanga"),
    ("Geita", "Geita"),

    ("Kigoma", "Kigoma"),
    ("Tabora", "Tabora"),
    ("Manyara", "Manyara"),
    ("Kilimanjaro", "Kilimanjaro"),
    ("Katavi", "Katavi"),

    ("Singida", "Singida"),
    ("Tanga", "Tanga"),
    ("Morogoro", "Morogoro"),
    ("Pwani", "Pwani"),
    ("Rukwa", "Rukwa"),

    ("Mbeya", "Mbeya"),
    ("Songwe", "Songwe"),
    ("Njombe", "Njombe"),
    ("Ruvuma", "Ruvuma"),
    ("Mtwara", "Mtwara"),

    ("Lindi", "Lindi"),
    ("Songwe", "Songwe"),

]
    user_type = [
    ("Doctor", "Doctor"),
    ("Nurse", "Nurse"),
]
    professional = [
    ("Eye", "Eye"),
    ("Teeth", "Teeth"),
    ("Other", "Other"),
]
    level = [
    ("Certificate", "Certificate"),
    ("Diploma", "Diploma"),
    ("Bachelor", "Bachelor"),
    ("Master", "Master"),
    ("Phd", "Phd"),
    ("Other", "Other"),
]
    
    sex = [
    ("Male", "Male"),
    ("Female", "Female"),
]

    user = models.ForeignKey(MyStaff, on_delete=models.CASCADE)
    User_type = models.CharField(max_length=40, choices=user_type)
    First_Name = models.CharField(max_length=100)
    Middle_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Sex = models.CharField(max_length=40, choices=sex)
    Level_Of_Education = models.CharField(max_length=40, choices=level)
    Professional = models.CharField(max_length=40, choices=professional)
    Region = models.CharField(max_length=40, choices=region)
    Phone = models.CharField(max_length=100)
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    
