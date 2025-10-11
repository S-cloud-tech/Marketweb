from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.conf import settings
from django.http import HttpResponse
from .forms import CustomUserCreationForm, CustomLoginForm
from .models import User
from .utils.activation_email import *

class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('authentication:login')  # adjust if namespaced

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True 
        user.save()

        otp, token = create_email_verification(user)
        send_activation_email(self.request, user, otp, token)

        messages.success(
            self.request,
            "Account created. We sent you an OTP and activation link."
        )
        return super().form_valid(form)  # handles redirect

# User Account Activation
def activate_user(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_object_or_404(User, pk=uid)
    except Exception:
        user = None

    if user and default_token_generator.check_token(user, token):
        user.is_active = True
        user.is_email_verified = True
        user.save()
        return redirect('login')
    return HttpResponse('Activation link is invalid!')


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = CustomLoginForm


# Redirect users based on their roles
def role_based_redirect(request):
        user = request.user
        if user.groups.filter(name='Salesperson').exists():
            return redirect('sales_dashboard')
        elif user.groups.filter(name='Inventory Manager').exists():
            return redirect('inventory_dashboard')
        elif user.is_superuser:
            return redirect('admin_dashboard')
        else:
            return redirect('home')

def logout_view(request):
    logout(request)
    return redirect("users:login")

class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'
