import uuid
from pathlib import Path

from django.conf import settings
from django.http import FileResponse, Http404
from django.views import View

RESUME_PATH = Path("others/resume_jona.pdf")

class ResumeDownloadView(View):
    def get(self, request):
        if not RESUME_PATH.exists():
            raise Http404()
        res = FileResponse(
            open(RESUME_PATH, "rb"),
            as_attachment=True,
            filename=f"resume_jona_{uuid.uuid4().hex[:8]}.pdf",
        )

        res['X-Robots-Tag'] = "noindex, nofollow, noarchive"
        return res
