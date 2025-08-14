# authentication/utils.py
import random
import hashlib
from django.core.cache import caches
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings

OTP_LENGTH = 6
OTP_TTL_SECONDS = 600       # 10 minutes
LINK_TTL_SECONDS = 86400    # 24 hours

otp_cache = caches["otp_cache"]

def generate_otp():
    return "".join(str(random.randint(0, 9)) for _ in range(OTP_LENGTH))

def hash_otp(otp: str, salt: str) -> str:
    return hashlib.sha256((salt + otp).encode()).hexdigest()

def create_email_verification(user):
    otp = generate_otp()
    otp_hash = hash_otp(otp, salt=str(user.pk))
    link_token = default_token_generator.make_token(user)

    otp_cache.set(f"otp:{user.pk}", otp_hash, timeout=OTP_TTL_SECONDS)
    otp_cache.set(f"link:{user.pk}", link_token, timeout=LINK_TTL_SECONDS)

    return otp, link_token

def send_activation_email(request, user, otp, link_token):
    activation_path = reverse("users:activate_by_link", kwargs={"uid": user.pk, "token": link_token})
    activation_url = request.build_absolute_uri(activation_path)

    subject = "Activate your account"
    message = (
        f"Hello {user.username},\n\n"
        f"Your OTP is: {otp} (valid for {OTP_TTL_SECONDS//60} minutes)\n"
        f"Or click this link to verify your email:\n{activation_url}\n\n"
        "If you did not request this, you can ignore this email."
    )
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email], fail_silently=False)
