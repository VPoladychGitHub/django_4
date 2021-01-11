from person.models import Log_midlware
from datetime import datetime


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        mas_path = request.path.split('/')
        if mas_path[1] == 'admin':
            return
        else:
            path_log = request.scheme + '://' + request.get_host() + request.path
            p = Log_midlware(path=path_log, method=request.method, timestamp=datetime.timestamp(datetime.now()))
            p.save()
