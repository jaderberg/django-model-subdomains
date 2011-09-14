import urlparse
from django import template
from django.template import Library
from django.template.defaulttags import URLNode, url
from django.contrib.sites.models import Site

register = Library()

class AbsoluteURLNode(URLNode):
    def render(self, context):
        path = super(AbsoluteURLNode, self).render(context)
        domain = "http://%s" % Site.objects.get_current().domain
        return urlparse.urljoin(domain, path)

def absurl(parser, token, node_cls=AbsoluteURLNode):
    """Just like {% url %} but ads the domain of the current site."""
    node_instance = url(parser, token)
    return node_cls(view_name=node_instance.view_name,
        args=node_instance.args,
        kwargs=node_instance.kwargs,
        asvar=node_instance.asvar)

absurl = register.tag(absurl)

class SubdomainAbsoluteURLNode(URLNode):
    def __init__(self, view_name, args, kwargs, asvar, legacy_view_name=True, subdomain_context=None):
        try:
            self.subdomain = template.Variable(subdomain_context)
        except template.VariableDoesNotExist:
            self.subdomain = ''
        super(SubdomainAbsoluteURLNode, self).__init__(view_name, args, kwargs, asvar, legacy_view_name)

    def render(self, context):
        path = super(SubdomainAbsoluteURLNode, self).render(context)
        domain = "http://%s.%s" % (self.subdomain.resolve(context), Site.objects.get_current().domain)
        return urlparse.urljoin(domain, path)

def suburl(parser, token, node_cls=SubdomainAbsoluteURLNode):
    """Just like {% url %} but ads the domain of the current site."""
    subdomain_context = token.split_contents()[2]
    
    token.contents = token.contents.replace(subdomain_context, '')
    node_instance = url(parser, token)
    return node_cls(view_name=node_instance.view_name,
        args=node_instance.args,
        kwargs=node_instance.kwargs,
        asvar=node_instance.asvar,
        subdomain_context=subdomain_context)

suburl = register.tag(suburl)
