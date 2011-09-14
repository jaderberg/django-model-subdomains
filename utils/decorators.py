from django.contrib.sites.models import Site
from django.http import HttpResponseRedirect

def base_site_url(view_fn):
    """
    Ensures that visitors to this view have done so from the base site url, not from a subdomain
    """

    def wrapper(request, *args, **kwargs):
        if request.subdomain:
            return HttpResponseRedirect('http://%s%s' % (Site.objects.get_current().domain, request.get_full_path()))
        return view_fn(request, *args, **kwargs)
    return wrapper

