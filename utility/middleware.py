from visitor.view_utils import visitorinfo_collect

class VisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.client_ip = visitorinfo_collect(request)
        response = self.get_response(request)

        return response
