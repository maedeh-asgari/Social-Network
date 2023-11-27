from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view

app_name = 'account'

urlpatterns = [
        #previous login
    #path('login/', views.user_login, name='login'),
    
        #login & logout
    #path('login/', auth_view.LoginView.as_view, name='login'),
    #path('logout/', auth_view.LogoutView.as_view, name='logout'),
        #change password
    #path('password-change/', auth_view.PasswordChangeView.as_view, name='password-change'),
    #path('password-change/done/', auth_view.PasswordChangeDoneView.as_view, name='password-change-done'),
        #reset password
    #path('password-reset/', auth_view.PasswordResetView.as_view, name='password-reset'),
    #path('password-reset-done/', auth_view.PasswordResetDoneView.as_view, name='password-reset-done'),
    #path('reset/<uid64>/<token>/', auth_view.PasswordResetConfirmView.as_view, name='password-reset-confirm'),
    #path('reset/done/', auth_view.PasswordResetCompleteView.as_view, name='password-reset-complete'),
    
    path('', include('django.contrib.auth.urls')),
    #path('', views.dashboard, name='dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('users/', views.user_list, name='user_list'),
    path('users/<username>', views.user_detail, name='user_detail'),
    path('users/follow/', views.user_follow, name='user_follow'),
]