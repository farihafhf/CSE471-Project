from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.home,name="home"),
    path("signup",views.signup, name="signup"),
    path("signin",views.signin, name="signin"),
    path("signout",views.signout, name="signout"),
    path('dashboard', views.dashboard, name='dashboard'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('view_profile/', views.view_profile, name='view_profile'),
    path('reset_password/', auth_views.PasswordResetView.as_view(),name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
]
