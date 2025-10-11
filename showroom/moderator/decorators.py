from django.shortcuts import redirect
from functools import wraps

def moderator_required(view_func):
    @wraps(view_func)
    def _wrapped(request, *args, **kwargs):
        if request.session.get('is_moderator'):
            return view_func(request, *args, **kwargs)
        return redirect('login_moderator')
    return _wrapped