# from django.contrib.auth.views import LoginView, LogoutView
# from django.shortcuts import redirect, get_object_or_404
# from django.urls import reverse_lazy
# from django.views.generic import CreateView, TemplateView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from .forms import CustomUserCreationForm, CustomLoginForm
# from django.core.mail import send_mail
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes
# from django.contrib.auth.tokens import default_token_generator
# from django.template.loader import render_to_string
# from django.conf import settings
# from django.http import HttpResponse
# from .models import User

# class RegisterView(CreateView):
#     template_name = 'users/register.html'
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')

#     def form_valid(self, form):
#         user = form.save(commit=False)
#         user.is_active = False
#         user.save()
        
#         uid = urlsafe_base64_encode(force_bytes(user.pk))
#         token = default_token_generator.make_token(user)

#         activation_link = self.request.build_absolute_uri(
#             reverse_lazy('activate', kwargs={'uidb64': uid, 'token': token})
#         )

#         message = render_to_string('users/email_verification.html', {
#             'user': user,
#             'activation_link': activation_link
#         })

#         send_mail(
#             'Verify your account',
#             message,
#             settings.DEFAULT_FROM_EMAIL,
#             [user.email],
#             fail_silently=False,
#         )

#         return redirect('login')

# # User Account Activation
# def activate_user(request, uidb64, token):
#     try:
#         uid = urlsafe_base64_decode(uidb64).decode()
#         user = get_object_or_404(User, pk=uid)
#     except Exception:
#         user = None

#     if user and default_token_generator.check_token(user, token):
#         user.is_active = True
#         user.is_email_verified = True
#         user.save()
#         return redirect('login')
#     return HttpResponse('Activation link is invalid!')


# class CustomLoginView(LoginView):
#     template_name = 'users/login.html'
#     authentication_form = CustomLoginForm


# # Redirect users based on their roles
# def role_based_redirect(request):
#         user = request.user
#         if user.groups.filter(name='Salesperson').exists():
#             return redirect('sales_dashboard')
#         elif user.groups.filter(name='Inventory Manager').exists():
#             return redirect('inventory_dashboard')
#         elif user.is_superuser:
#             return redirect('admin_dashboard')
#         else:
#             return redirect('home')

# class CustomLogoutView(LogoutView):
#     next_page = reverse_lazy('login')

# class UserProfileView(LoginRequiredMixin, TemplateView):
#     template_name = 'users/profile.html'
