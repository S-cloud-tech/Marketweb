# core/context_processors.py
from .models import GeneralInfo, About

def site_info(request):
    return {
        "general_info": GeneralInfo.objects.first(),   # expects only 1 record
        "about": About.objects.first(),                # same for About
    }
