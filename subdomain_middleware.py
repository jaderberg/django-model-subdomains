from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, Http404
from subdomain_settings import *

class SubdomainMiddleware:
    def process_request(self, request):
        """
        Intercepts request and processes subdomain.
        Only works with a single subdomain (e.g. lol.jk.com, not a.lol.jk.com)
        """
        request.subdomain = None
        host = request.META.get('HTTP_HOST', '')
        host_s = host.replace('www.', '').split('.')
        if len(host_s) > 2:
            request.subdomain = host_s[0]
        if request.subdomain:
            # A subdomain exists. First try and match subdomains not in the model
            sub = request.subdomain
            try:
                #try to find a subdomain in this list (not a model subdomain)
                request.urlconf = SUBDOMAIN_URLCONFS[sub]
            except KeyError:
                try:
                    #try and find a model associated with this subdomain
                    request.subdomain_object = MODEL_TO_SUBDOMAIN['model'].objects.get(**{MODEL_TO_SUBDOMAIN['filter_field'] : sub})
                    request.urlconf = MODEL_TO_SUBDOMAIN['url_conf']
                except ObjectDoesNotExist:
                    if REDIRECT_IF_NO_MODEL:
                        return HttpResponseRedirect(REDIRECT_IF_NO_MODEL)
                    else:
                        raise Http404