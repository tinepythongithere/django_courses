from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

def group_required(group_name):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.groups.filter(name=group_name).exists():
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("You do not have permission to access this page.")
        return login_required(_wrapped_view)
    return decorator
