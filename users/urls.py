# from django.urls import path
# from django.contrib.auth import views as auth_views
# from . import views

# app_name =  'users'

# urlpatterns = [
#     path('register/', views.RegisterView.as_view(), name='register'),
#     path('login/', views.CustomLoginView.as_view(), name='login'),
#     path('redirect-after-login/', views.role_based_redirect, name='role_redirect'),
#     path('logout/', views.CustomLogoutView.as_view(), name='logout'),
#     path('profile/', views.UserProfileView.as_view(), name='profile'),
#     path('activate/<uidb64>/<token>/', views.activate_user, name='activate'),
#     path('password-reset/', auth_views.PasswordResetView.as_view(
#         template_name='users/password_reset.html'), name='password_reset'),
#     path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
#         template_name='users/password_reset_done.html'), name='password_reset_done'),
#     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
#         template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
#     path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
#         template_name='users/password_reset_complete.html'), name='password_reset_complete'),
# ]
