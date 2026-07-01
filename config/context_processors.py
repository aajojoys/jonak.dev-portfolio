from django.conf import settings

def global_settings(request):
    return {
        "TURNSTILE_SITEKEY": settings.TURNSTILE_SITEKEY,
    }
