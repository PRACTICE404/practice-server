from django.shortcuts import redirect


class SubdomainMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().split(':')[0]  # Избавляемся от порта
        if host == 'blog.aleksdev.xyz' and not request.path.startswith('/blog/'):  # noqa
            return redirect(f"/blog{request.path}")
        return self.get_response(request)
