from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/addstudent/', views.add_student, name='addstudent'),
    path('dashboard/train/', views.train_database, name='train'),
    path('dashboard/takeattendance/', views.take_attendance, name='takeattendance'),
    path('dashboard/view/', views.view_attendance, name='view'),
    path('dashboard/settings/', views.settings, name='settings'),
    path('dashboard/sendmail/', views.send_mail, name='sendmail'),
    path('dashboard/profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('api/chart/data/', views.ChartData.as_view()),
]
