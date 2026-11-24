from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('report/', views.report_waste_view, name='report_waste'),
    path('my-reports/', views.my_complaints_view, name='my_complaints'),
    path('report/<int:pk>/', views.complaint_detail_view, name='complaint_detail'),
]
