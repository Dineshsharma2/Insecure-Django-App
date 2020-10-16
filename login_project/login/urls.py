from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.loginscreen),
    path('', views.loginpage, name='login'),
    path('log/', views.loginsuccess,name='admin'),
    path('sqli/', views.sqli,name='sqli'),
    path('sqli_vuln/', views.sqli_vuln,name='sqlivuln'),
    path('xss_vuln/', views.xss_vuln,name='xssvuln'),
    path('csrf_vuln/', views.csrf_vuln,name='csrfvuln'),
    path('file_vuln/', views.file_vuln,name='filevuln'),
    path('editprofile/',views.editprofile,name='editprofile'),
	path('cmdi_vuln/',views.cmdi_vuln,name='cmdivuln'),
	path('lfi_vul/',views.lfi_vul,name='lfivul'),
	path('lfi_vuln/',views.lfi_vuln,name='lfivuln'),
    path('file_vuln/',views.file_vuln,name='fileupload'),


]
