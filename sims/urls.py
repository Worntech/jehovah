from django.urls import path
from . import views

from .views import change_password

# from .views import update_clinics_view

urlpatterns = [
    # path('signup/', views.signup, name = "signup"),
    path('addstudents/', views.addstudents, name = "addstudents"),
    path('addstaff/', views.addstaff, name = "addstaff"),
    # path('signin/', views.signin, name = "signin"),
    path('signinsims/', views.signinsims, name = "signinsims"),
	path('logout/', views.logout, name="logout"),
 
 
    path('news/', views.news, name = "news"),
    path('', views.dashboard, name = "dashboard"),
    
    path('student/', views.student, name = "student"),
    # path('viewpatient/<str:pk>/', views.viewpatient.as_view(), name = "viewpatient"),
    path('staff/', views.staff, name = "staff"),
    path('studentaccount/', views.studentaccount, name = "studentaccount"),
    path('payment/', views.payment, name = "payment"),
    path('profile/', views.profile, name = "profile"),
    path('myprofile/', views.myprofile, name = "myprofile"),
    path('base/', views.base, name = "base"),
    
    path('addstudent/', views.addstudent, name = "addstudent"),
    path('addresult/', views.addresult, name = "addresult"),
    path('addpayment/', views.addpayment, name = "addpayment"),
    path('addstaffcontactinfo/', views.addstaffcontactinfo, name = "addstaffcontactinfo"),
    # path('studentaccount/', views.studentaccount, name = "studentaccount"),

    # url for viewing
    path("viewstudentaccount/<int:id>/",views.viewstudentaccount,name = "viewstudentaccount"),
    # path("viewpatient/<int:id>/",views.viewpatient,name = "viewpatient"),
    path("viewstaffinfo/<int:id>/",views.viewstaffinfo,name = "viewstaffinfo"),
    
    # url for updating the information
    path('updatestudent/<int:pk>/', views.updatestudent, name = "updatestudent"),
    path('updateresult/<int:pk>/', views.updateresult, name = "updateresult"),
    path('updatepayment/<int:pk>/', views.updatepayment, name = "updatepayment"),
    
    path('updatestaffcontactinfo/<int:id>/', views.updatestaffcontactinfo, name = "updatestaffcontactinfo"),
    path('updatestudentaccount/<int:id>/', views.updatestudentaccount, name = "updatestudentaccount"),
    
    # url for deletting information
    path('deletestudent/<int:pk>/', views.deletestudent, name = "deletestudent"),
    path('deleteresult/<int:pk>/', views.deleteresult, name = "deleteresult"),
    path('deletepayment/<int:pk>/', views.deletepayment, name = "deletepayment"),
    
    path('deletestaffcontactinfo/<int:id>/', views.deletestaffcontactinfo, name = "deletestaffcontactinfo"),
    path('deletestudentaccount/<int:id>/', views.deletestudentaccount, name = "deletestudentaccount"),
    
    path('change-password/', change_password, name='change_password'),
    
    # FOR EXPORTING TO WORD, PDF AND EXCEL
    path('export/patients/csv/', views.export_patients_to_csv, name='export_patients_csv'),
    path('export/patients/pdf/', views.export_patients_to_pdf, name='export_patients_pdf'),
    path('export/patients/excel/', views.export_patients_to_excel, name='export_patients_excel'),
    
    # FOR EXPORTING TO WORD, PDF AND EXCEL FOR STAFF
    path('export/staffs/csv/', views.export_staff_to_csv, name='export_staff_csv'),
    path('export/staffs/pdf/', views.export_staff_to_pdf, name='export_staff_pdf'),
    path('export/staffs/excel/', views.export_staff_to_excel, name='export_staff_excel'),
    
    # UPDATING MEDICAL TREATMENT
    # path('update/<int:instance_id>/', update_clinics_view, name='update_instance'),
    
    path('studentone/', views.studentone, name = "studentone"),
    path('studenttwo/', views.studenttwo, name = "studenttwo"),
    path('studentthree/', views.studentthree, name = "studentthree"),
    path('studentfour/', views.studentfour, name = "studentfour"),
    path('studentfive/', views.studentfive, name = "studentfive"),
    path('studentsix/', views.studentsix, name = "studentsix"),
    path('studentseven/', views.studentseven, name = "studentseven"),
    
    path('resultone/', views.resultone, name = "resultone"),
    path('resulttwo/', views.resulttwo, name = "resulttwo"),
    path('resultthree/', views.resultthree, name = "resultthree"),
    path('resultfour/', views.resultfour, name = "resultfour"),
    path('resultfive/', views.resultfive, name = "resultfive"),
    path('resultsix/', views.resultsix, name = "resultsix"),
    path('resultseven/', views.resultseven, name = "resultseven"),
    
    path('paymentone/', views.paymentone, name = "paymentone"),
    path('paymenttwo/', views.paymenttwo, name = "paymenttwo"),
    path('paymentthree/', views.paymentthree, name = "paymentthree"),
    path('paymentfour/', views.paymentfour, name = "paymentfour"),
    path('paymentfive/', views.paymentfive, name = "paymentfive"),
    path('paymentsix/', views.paymentsix, name = "paymentsix"),
    path('paymentseven/', views.paymentseven, name = "paymentseven"),
    

]
