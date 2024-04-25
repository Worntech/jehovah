from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User, auth
from . models import *
from . forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView

from django.conf import settings

from web.views import *

from django.shortcuts import render, get_object_or_404
from django.http import Http404

from django.contrib.auth import get_user_model

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from django.db.models import Sum
from django.shortcuts import get_list_or_404

# FOR PRINTING TABLE
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.text import slugify
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from openpyxl import Workbook
from .models import Student
from .models import StaffContactinfo

# UPDATING THE MEDICAL TREATMENT
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
# @login_required(login_url='signin')
def admin(request):
    return render(request, 'sims/admin.html')
@login_required(login_url='signinsims')
def addstudents(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        # id = request.POST.get('id')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if MyStaff.objects.filter(email=email).exists():
                messages.info(request, f"Email {email} Already Taken")
                return redirect('addstudents')
            elif MyStaff.objects.filter(username=username).exists():
                messages.info(request, f"Id Number {username} Already Taken")
                return redirect('addstudents')
            else:
                user = MyStaff.objects.create_user(username=username, email=email, password=password)
                user.save()
                # messages.info(request, 'Registered Student Succesefull.')
                return redirect('addPatient')
        else:
            messages.info(request, 'The Two Passwords Not Matching')
            return redirect('addstudents')

    else:
        return render(request, 'sims/addstudents.html')
    
# @login_required(login_url='signinsims')
def addstaff(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        # id = request.POST.get('id')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if MyStaff.objects.filter(email=email).exists():
                messages.info(request, f"Email {email} Already Taken")
                return redirect('addstaff')
            elif MyStaff.objects.filter(username=username).exists():
                messages.info(request, f"Id Number {username} Already Taken")
                return redirect('addstaff')
            else:
                user = MyStaff.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.info(request, 'Registered Staff Succesefull.')
                return redirect('addstaffcontactinfo')
        else:
            messages.info(request, 'The Two Passwords Not Matching')
            return redirect('addstaff')

    else:
        return render(request, 'sims/addstaff.html')


def signinsims(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            # messages.info(request, 'Loged in succesefull.')
            return redirect('dashboard')
        else:
            messages.info(request, 'Username or password is incorrect')
            return redirect('signinsims')

    else:
        return render(request, 'sims/signinsims.html')

@login_required(login_url='signinsims')
def logout(request):
    auth.logout(request)
    messages.info(request, 'Loged out succesefull.')
    return redirect('signinsims')

@login_required(login_url='signinsims')
def news(request):
    return render(request, 'sims/news.html')

@login_required(login_url='signinsims')
def dashboard(request):
    countstudent= Student.objects.all().count()
    # count_nhif_patients = Student.objects.filter(Payment='NHIF').count()
    # count_cash_patients = Student.objects.filter(Payment='Cash payment').count()
    countstaff= StaffContactinfo.objects.all().count()
    context={
        "countstudent":countstudent,
        "countstaff":countstaff,
        # "count_nhif_patients":count_nhif_patients,
        # "count_cash_patients":count_cash_patients,
    }
    return render(request, 'sims/dashboard.html', context)

# def base(request):
#     # Assuming 'username' is the attribute in MyStaff that corresponds to the user's username
#     logged_in_user = MyStaff.objects.get(username=request.user.username)

#     # Fetching CA results related to the logged-in user using the obtained 'logged_in_user' instance
#     profilename = Patient.objects.filter(Ca_Number__user=logged_in_user)
    
#     context={
#         "profilename":profilename,
#         # "countstaff":countstaff
#     }
#     return render(request, 'sims/base.html', context)

@login_required(login_url='signinsims')
def base(request):
    # Assuming 'username' is the attribute in MyStaff that corresponds to the user's username
    logged_in_user = MyStaff.objects.get(username=request.user.username)

    # Fetching related Patient for the logged-in user
    student_contact_info = Student.objects.filter(user=logged_in_user).first()

    if student_contact_info:
        # Accessing first name and last name from Patient
        first_name = student_contact_info.First_Name
        last_name = student_contact_info.Last_Name

        return render(request, 'sims/base.html', {'first_name': first_name, 'last_name': last_name})
    else:
        # Handle scenario where there's no related Patient
        return render(request, 'sims/base.html')  


@login_required(login_url='signinsims')
def student(request):
    student = Student.objects.all().order_by("-pk")
    context={
        "student":student
    }
    return render(request, 'sims/student.html', context)

@login_required(login_url='signinsims')
def studentone(request):
    studentone = Student.objects.all().order_by("-pk")
    context={
        "studentone":studentone
    }
    return render(request, 'sims/studentone.html', context)

@login_required(login_url='signinsims')
def studenttwo(request):
    studenttwo = Student.objects.all().order_by("-pk")
    context={
        "studenttwo":studenttwo
    }
    return render(request, 'sims/studenttwo.html', context)

@login_required(login_url='signinsims')
def studentthree(request):
    studentthree = Student.objects.all().order_by("-pk")
    context={
        "studentthree":studentthree
    }
    return render(request, 'sims/studentthree.html', context)

@login_required(login_url='signinsims')
def studentfour(request):
    studentfour = Student.objects.all().order_by("-pk")
    context={
        "studentfour":studentfour
    }
    return render(request, 'sims/studentfour.html', context)

@login_required(login_url='signinsims')
def studentfive(request):
    studentfive = Student.objects.all().order_by("-pk")
    context={
        "studentfive":studentfive
    }
    return render(request, 'sims/studentfive.html', context)

@login_required(login_url='signinsims')
def studentsix(request):
    studentsix = Student.objects.all().order_by("-pk")
    context={
        "studentsix":studentsix
    }
    return render(request, 'sims/studentsix.html', context)

@login_required(login_url='signinsims')
def studentseven(request):
    studentseven = Student.objects.all().order_by("-pk")
    context={
        "studentseven":studentseven
    }
    return render(request, 'sims/studentseven.html', context)

# RESULT
@login_required(login_url='signinsims')
def resultone(request):
    resultone = Result.objects.all().order_by("-pk")
    context={
        "resultone":resultone
    }
    return render(request, 'sims/resultone.html', context)

@login_required(login_url='signinsims')
def resulttwo(request):
    resulttwo = Result.objects.all().order_by("-pk")
    context={
        "resulttwo":resulttwo
    }
    return render(request, 'sims/resulttwo.html', context)

@login_required(login_url='signinsims')
def resultthree(request):
    resultthree = Result.objects.all().order_by("-pk")
    context={
        "resultthree":resultthree
    }
    return render(request, 'sims/resultthree.html', context)

@login_required(login_url='signinsims')
def resultfour(request):
    resultfour = Result.objects.all().order_by("-pk")
    context={
        "resultfour":resultfour
    }
    return render(request, 'sims/resultfour.html', context)

@login_required(login_url='signinsims')
def resultfive(request):
    resultfive = Result.objects.all().order_by("-pk")
    context={
        "resultfive":resultfive
    }
    return render(request, 'sims/resultfive.html', context)

@login_required(login_url='signinsims')
def resultsix(request):
    resultsix = Result.objects.all().order_by("-pk")
    context={
        "resultsix":resultsix
    }
    return render(request, 'sims/resultsix.html', context)

@login_required(login_url='signinsims')
def resultseven(request):
    resultseven = Result.objects.all().order_by("-pk")
    context={
        "resultseven":resultseven
    }
    return render(request, 'sims/resultseven.html', context)

# FOR PAYMENT
@login_required(login_url='signinsims')
def payment(request):
    payment = Payment.objects.all().order_by("-pk")
    context={
        "payment":payment
    }
    return render(request, 'sims/payment.html', context)


@login_required(login_url='signinsims')
def paymentone(request):
    paymentone = Payment.objects.all().order_by("-pk")
    context={
        "paymentone":paymentone
    }
    return render(request, 'sims/paymentone.html', context)

@login_required(login_url='signinsims')
def paymenttwo(request):
    paymenttwo = Payment.objects.all().order_by("-pk")
    context={
        "paymenttwo":paymenttwo
    }
    return render(request, 'sims/paymenttwo.html', context)

@login_required(login_url='signinsims')
def paymentthree(request):
    paymentthree = Payment.objects.all().order_by("-pk")
    context={
        "paymentthree":paymentthree
    }
    return render(request, 'sims/paymentthree.html', context)

@login_required(login_url='signinsims')
def paymentfour(request):
    paymentfour = Payment.objects.all().order_by("-pk")
    context={
        "paymentfour":paymentfour
    }
    return render(request, 'sims/paymentfour.html', context)

@login_required(login_url='signinsims')
def paymentfive(request):
    paymentfive = Payment.objects.all().order_by("-pk")
    context={
        "paymentfive":paymentfive
    }
    return render(request, 'sims/paymentfive.html', context)

@login_required(login_url='signinsims')
def paymentsix(request):
    paymentsix = Payment.objects.all().order_by("-pk")
    context={
        "paymentsix":paymentsix
    }
    return render(request, 'sims/paymentsix.html', context)

@login_required(login_url='signinsims')
def paymentseven(request):
    paymentseven = Payment.objects.all().order_by("-pk")
    context={
        "paymentseven":paymentseven
    }
    return render(request, 'sims/paymentseven.html', context)


@login_required(login_url='signinsims')
def studentaccount(request):
    studentaccount = MyStaff.objects.all()
    # countstaff= MyStaff.objects.all().count()
    context={
        "studentaccount":studentaccount,
        # "countstaff":countstaff
    }
    return render(request, 'sims/studentaccount.html', context)

@login_required(login_url='signinsims')
def staff(request):
    stafflist = StaffContactinfo.objects.all().order_by("-pk")
    # countstaff= MyStaff.objects.all().count()
    context={
        "stafflist":stafflist,
        # "countstaff":countstaff
    }
    return render(request, 'sims/staff.html', context)


@login_required(login_url='signinsims')
def news(request):
    return render(request, 'sims/news.html')

@login_required(login_url='signinsims')
def profile(request):
    current_user = request.user
    
    try:
        user_instance = get_object_or_404(MyStaff, username=current_user.username)
        Patient= Patient.objects.filter(user=user_instance)

        context={
            "Patient":Patient,
            "user_instance":user_instance,
            "current_user":current_user
        }
        return render(request, 'sims/profile.html', context)

    except MyStaff.DoesNotExist:
        raise Http404("User does not exist")  # Handle case where user is not found

@login_required(login_url='signinsims')
def myprofile(request):
    current_user = request.user
    
    try:
        user_instance = get_object_or_404(MyStaff, username=current_user.username)
        staffcontactinfo= StaffContactinfo.objects.filter(user=user_instance)

        context={
            "staffcontactinfo":staffcontactinfo,
            "user_instance":user_instance,
            "current_user":current_user
        }
        return render(request, 'sims/myprofile.html', context)

    except MyStaff.DoesNotExist:
        raise Http404("User does not exist")  # Handle case where user is not found

@login_required(login_url='signinsims')
def addstudent(request):
    student = StudentForm()
    if request.method == "POST":
        student = StudentForm(request.POST, files=request.FILES)
        if student.is_valid():
            student.save()
            messages.info(request, 'student Added Succesefull.')
            return redirect('addstudent')

    context={
        "student":student
    }
    return render(request, 'sims/addstudent.html', context)

@login_required(login_url='signinsims')
def addresult(request):
    result = ResultForm()
    if request.method == "POST":
        result = ResultForm(request.POST, files=request.FILES)
        if result.is_valid():
            result.save()
            messages.info(request, 'result Added Succesefull.')
            return redirect('addresult')

    context={
        "result":result
    }
    return render(request, 'sims/addresult.html', context)

def addpayment(request):
    payment = PaymentForm()
    if request.method == "POST":
        payment = PaymentForm(request.POST, files=request.FILES)
        if payment.is_valid():
            payment.save()
            messages.info(request, 'payment Added Succesefull.')
            return redirect('addpayment')

    context={
        "payment":payment
    }
    return render(request, 'sims/addpayment.html', context)

@login_required(login_url='signinsims')
def addstaffcontactinfo(request):
    staffcontactinfo = StaffContactinfoForm()
    if request.method == "POST":
        staffcontactinfo = StaffContactinfoForm(request.POST, files=request.FILES)
        if staffcontactinfo.is_valid():
            staffcontactinfo.save()
            messages.info(request, 'Student Registered Succesefull.')
            return redirect('addstaff')

    context={
        "staffcontactinfo":staffcontactinfo
    }
    return render(request, 'sims/addstaffcontactinfo.html', context)

# views for viewing
@login_required(login_url='signinsims')
def viewstudentaccount(request, id):
    studentaccountview = MyStaff.objects.get(id=id)
    
    context = {"studentaccountview":studentaccountview}
    return render(request, 'sims/viewstudentaccount.html', context)

@login_required(login_url='signinsims')
def viewpatientinfo(request, id):
    patientinfoview = Student.objects.get(id=id)
    
    context = {"patientinfoview":patientinfoview}
    return render(request, 'sims/viewpatientinfo.html', context)

@login_required(login_url='signinsims')
def viewstaffinfo(request, id):
    staffinfoview = StaffContactinfo.objects.get(id=id)
    
    context = {"staffinfoview":staffinfoview}
    return render(request, 'sims/viewstaffinfo.html', context)

# view for updating the information
@login_required(login_url='signinsims')
def updatestudent(request, pk):
    a = Student.objects.get(pk=pk)
    student =StudentForm(instance=a)
    if request.method == "POST":
        student = StudentForm(request.POST, files=request.FILES, instance=a)
        if student.is_valid():
            student.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('student')
    context = {"student":student}
    return render(request, 'sims/updatestudent.html', context)

@login_required(login_url='signinsims')
def updateresult(request, pk):
    z = Result.objects.get(pk=pk)
    result =ResultForm(instance=z)
    if request.method == "POST":
        result = ResultForm(request.POST, files=request.FILES, instance=z)
        if result.is_valid():
            result.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('resultone')
    context = {"result":result}
    return render(request, 'sims/updateresult.html', context)

@login_required(login_url='signinsims')
def updatepayment(request, pk):
    y = Payment.objects.get(pk=pk)
    payment =PaymentForm(instance=y)
    if request.method == "POST":
        payment = PaymentForm(request.POST, files=request.FILES, instance=y)
        if payment.is_valid():
            payment.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('payment')
    context = {"payment":payment}
    return render(request, 'sims/updatepayment.html', context)

@login_required(login_url='signinsims')
def updatestaffcontactinfo(request, id):
    b = StaffContactinfo.objects.get(id=id)
    staffinfo =StaffContactinfoForm(instance=b)
    if request.method == "POST":
        staffinfo = StaffContactinfoForm(request.POST, files=request.FILES, instance=b)
        if staffinfo.is_valid():
            staffinfo.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('staff')
    context = {"staffinfo":staffinfo}
    return render(request, 'sims/updatestaffcontactinfo.html', context)

@login_required(login_url='signinsims')
def updatestudentaccount(request, id):
    c = MyStaff.objects.get(id=id)
    studentaccount =MyStaffForm(instance=c)
    if request.method == "POST":
        studentaccount = MyStaffForm(request.POST, files=request.FILES, instance=c)
    if studentaccount.is_valid():
        cleaned_data = studentaccount.cleaned_data
        # Check if the new username is different from the existing one
        if 'username' in cleaned_data and cleaned_data['username'] != c.username:
            # If it's different, update the instance and save
            c.username = cleaned_data['username']
            c.save()
            messages.info(request, 'Updated successfully.')
            return redirect('students')
        else:
            # Username remains unchanged, proceed without modifying
            messages.info(request, 'No changes made.')
            return redirect('students')
    context = {"studentaccount":studentaccount}
    return render(request, 'sims/updatestudentaccount.html', context)

# view for deleting information
@login_required(login_url='signinsims')
def deletestudent(request, pk):
    studentdelete = Student.objects.get(pk=pk)
    if request.method == "POST":
        studentdelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('student')
    
    context = {"studentdelete":studentdelete}
    return render(request, 'sims/deletestudent.html', context)

@login_required(login_url='signinsims')
def deleteresult(request, pk):
    resultdelete = Result.objects.get(pk=pk)
    if request.method == "POST":
        resultdelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('result')
    
    context = {"resultdelete":resultdelete}
    return render(request, 'sims/deleteresult.html', context)

@login_required(login_url='signinsims')
def deletepayment(request, pk):
    paymentdelete = Payment.objects.get(pk=pk)
    if request.method == "POST":
        paymentdelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('student')
    
    context = {"paymentdelete":paymentdelete}
    return render(request, 'sims/deletepayment.html', context)

@login_required(login_url='signinsims')
def deletestaffcontactinfo(request, id):
    staffcontactinfodelete = StaffContactinfo.objects.get(id=id)
    if request.method == "POST":
        staffcontactinfodelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('staff')
    
    context = {"staffcontactinfodelete":staffcontactinfodelete}
    return render(request, 'sims/deletestaffcontactinfo.html', context)

@login_required(login_url='signinsims')
def deletestudentaccount(request, id):
    studentaccountdelete = MyStaff.objects.get(id=id)
    if request.method == "POST":
        studentaccountdelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('studentaccount')
    
    context = {"studentaccountdelete":studentaccountdelete}
    return render(request, 'sims/deletestudentaccount.html', context)


@login_required(login_url='signinsims')
def change_password(request):
    if request.method == 'POST':
        passwordchange = PasswordChangeForm(request.user, request.POST)
        if passwordchange.is_valid():
            user = passwordchange.save()
            # This is to keep the user logged in after password change
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('signinsims')  # Redirect to the same page after successful password change
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        passwordchange = PasswordChangeForm(request.user)
    return render(request, 'sims/change_password.html', {'passwordchange': passwordchange})


# FOR PRINTING ALL TABLES

def export_patients_to_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="patients.csv"'

    patients = Student.objects.all()

    header = ['Patient ID', 'First Name', 'Middle Name', 'Last Name', 'Sex', 'Place', 'Age', 'Phone', 'Payment', 'Cost', 'Date']
    csv_data = ','.join(header) + '\n'
    for patient in patients:
        csv_data += ','.join([
            patient.Patient_Id,
            patient.First_Name,
            patient.Middle_Name,
            patient.Last_Name,
            patient.Sex,
            patient.Place,
            patient.Age,
            patient.Phone,
            patient.Payment,
            patient.Cost,
            patient.date_joined.strftime('%Y-%m-%d %H:%M:%S')
        ]) + '\n'

    response.write(csv_data)
    return response

def export_patients_to_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="patients.pdf"'

    patients = Student.objects.all()

    table_data = [['Patient ID', 'First Name', 'Middle Name', 'Last Name', 'Sex', 'Place', 'Age', 'Phone', 'Payment', 'Cost', 'Date']]
    for patient in patients:
        table_data.append([
            patient.Patient_Id,
            patient.First_Name,
            patient.Middle_Name,
            patient.Last_Name,
            patient.Sex,
            patient.Place,
            patient.Age,
            patient.Phone,
            patient.Payment,
            patient.Cost,
            patient.date_joined.strftime('%Y-%m-%d %H:%M:%S')
        ])

    doc = SimpleDocTemplate(response, pagesize=letter)
    table = Table(table_data)

    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.setStyle(style)
    doc.build([table])

    return response

def export_patients_to_excel(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="patients.xlsx"'

    patients = Student.objects.all()

    wb = Workbook()
    ws = wb.active

    ws.append(['Patient ID', 'First Name', 'Middle Name', 'Last Name', 'Sex', 'Place', 'Age', 'Phone', 'Payment', 'Cost', 'Date'])
    for patient in patients:
        ws.append([
            patient.Patient_Id,
            patient.First_Name,
            patient.Middle_Name,
            patient.Last_Name,
            patient.Sex,
            patient.Place,
            patient.Age,
            patient.Phone,
            patient.Payment,
            patient.Cost,
            patient.date_joined.strftime('%Y-%m-%d %H:%M:%S')
        ])

    wb.save(response)
    return response




# FOR PRINTING ALL TABLES OF STAFF CONTACT INFORMATION

def export_staff_to_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="staff.csv"'

    staffs = StaffContactinfo.objects.all()

    header = ['Staff ID', 'First Name', 'Middle Name', 'Last Name', 'Sex', 'Level_Of_Education', 'Professional', 'Phone', 'Region', 'Date']
    csv_data = ','.join(header) + '\n'
    for staff in staffs:
        csv_data += ','.join([
            staff.user.username if staff.user else '',
            staff.First_Name,
            staff.Middle_Name,
            staff.Last_Name,
            staff.Sex,
            staff.Level_Of_Education,
            staff.Professional,
            staff.Phone,
            staff.Region,
            staff.date_joined.strftime('%Y-%m-%d %H:%M:%S')
        ]) + '\n'

    response.write(csv_data)
    return response

def export_staff_to_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="staff.pdf"'

    staffs = StaffContactinfo.objects.all()

    table_data = [['Staff ID', 'First Name', 'Middle Name', 'Last Name', 'Sex', 'Level_Of_Education', 'Professional', 'Phone', 'Region', 'Date']]
    for staff in staffs:
        table_data.append([
            staff.user,
            staff.First_Name,
            staff.Middle_Name,
            staff.Last_Name,
            staff.Sex,
            staff.Level_Of_Education,
            staff.Professional,
            staff.Phone,
            staff.Region,
            staff.date_joined.strftime('%Y-%m-%d %H:%M:%S')
        ])

    doc = SimpleDocTemplate(response, pagesize=letter)
    table = Table(table_data)

    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.setStyle(style)
    doc.build([table])

    return response

def export_staff_to_excel(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="staff.xlsx"'

    staffs = StaffContactinfo.objects.all()

    wb = Workbook()
    ws = wb.active

    ws.append(['Staff ID', 'First Name', 'Middle Name', 'Last Name', 'Sex', 'Level_Of_Education', 'Professional', 'Phone', 'Region', 'Date'])
    for staff in staffs:
        ws.append([
            staff.user.username if staff.user else '',
            staff.First_Name,
            staff.Middle_Name,
            staff.Last_Name,
            staff.Sex,
            staff.Level_Of_Education,
            staff.Professional,
            staff.Phone,
            staff.Region,
            staff.date_joined.strftime('%Y-%m-%d %H:%M:%S')
        ])

    wb.save(response)
    return response

