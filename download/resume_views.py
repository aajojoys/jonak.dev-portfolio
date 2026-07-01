import uuid, requests
from pathlib import Path

from django.conf import settings from django.http import FileResponse, JsonResponse, Http404
from django.views import View
from django.core import signing

RESUME_PATH = Path("others/resume_jona.pdf")
CLOUDFLARE_LINK = "https://challenges.cloudflare.com/turnstile/v0/siteverify"

def verify_turnstile(request):
    token = request.POST.get("cf-turnstile-response")
    if not token: return False
    res = requests.post(
        CLOUDFLARE_LINK,
        data=dict(secret=settings.TURNSTILE_SECRETKEY, response=token, remoteip=request.META.get("HTTP_X_FORWARDED_FOR")),
        timeout=5,
    )
    result = res.json()
    return result.get("success", False)

class ResumeDownloadView(View):
    def post(self, request):
        if not verify_turnstile(request):
            return HttpResponseForbidden("Turnstile verification failed")

        token = signing.dumps(dict(resume=True), salt="resume-download")
        return JsonResponse({'download_url': f"/download/resume/?token={token}"})

    def get(self, request):
        token = request.GET.get("token")

        if not token:
            return HttpResponseForbidden()
        try:
            signing.loads(token, salt="resume-download", max_age=300)
        except signing.BadSignature:
            return HttpResponseForbidden()
        except signing.Expired:
            return HttpResponseForbidden()

        if not RESUME_PATH.exists():
            raise Http404()
        res = FileResponse(
            open(RESUME_PATH, "rb"),
            as_attachment=True,
            filename=f"resume_jona_{uuid.uuid4().hex[:8]}.pdf",
        )

        res['X-Robots-Tag'] = "noindex, nofollow, noarchive"
        return res
