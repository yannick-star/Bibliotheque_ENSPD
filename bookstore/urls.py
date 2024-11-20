from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [


    path('', views.login_form, name='home'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('regform/', views.register_form, name='regform'),
    path('register/', views.registerView, name='register'),
    


    path('librarian/', views.librarian, name='librarian'),
    



    path('publisher/', views.UBookListView.as_view(), name='publisher'),
    path('uabook_form/', views.uabook_form, name='uabook_form'),
    path('uabook/', views.uabook, name='uabook'),


    path('dashboard/', views.dashboard, name='dashboard'),
    path('aabook_form/', views.aabook_form, name='aabook_form'),
    path('aabook/', views.aabook, name='aabook'),
    path('albook/', views.ABookListView.as_view(), name='albook'),
]