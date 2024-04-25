from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class MyStudentsForm(UserCreationForm):
    class Meta:
        model = MyStudents
        fields = ['email', 'username']
        
class MyStaffForm(UserCreationForm):
    class Meta:
        model = MyStaff
        fields = ['email', 'username']
        
class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        
class ResultForm(ModelForm):
    class Meta:
        model = Result
        fields = '__all__'
        
class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
           
class StaffContactinfoForm(ModelForm):
    class Meta:
        model = StaffContactinfo
        fields = '__all__'
