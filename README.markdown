#django-model-subdomains

This middleware allow models to have subdomains, to create for example username.yoursite.com style websites.

First other subdomains are checked (e.g. blog.yoursite.com, api.yoursite.com) before model objects are.

If a subdomain is matched, the url conf associated with that subdomain is used for all requests, the subdomains is added to the request object (request.subdomain) and if a model is matched, the object is added to the request object for use in views (request.subdomain_object).

## Installation

1. Copy subdomain_middleware.py and subdomain_settings.py into your project.
2. Add 'subdomain_middleware.SubdomainMiddleware' to your MIDDLEWARE_CLASSES in your project settings.py file.
3. Optional: Add 'utils' to installed apps.
4. Set up the subdomain_settings.py file - set up the model you want to subdomain, as well as the url_confs for the model subdomains and other subdomains.
5. Create the url confs needed for the subdomains. 

## Example Configuration

An example configuration is included with model_urls.py being the url conf used if a model is matched on a subdomain, otherwise the default urls.py is used. 

## Settings

MODEL_TO_SUBDOMAIN takes two fields, 'model' and 'filter_field' which should take the model type and the name of the field to filter using the subdomain to find the associated model.

MODEL_SUBDOMAIN_URLCONF is the url conf to use if a model is found.

SUBDOMAIN_URLCONFS takes subdomain names and the associated url conf to use if a match is found. These subdomains are matched prior to any models (so make sure noone has a username 'blog' for example).

REDIRECT_IF_NO_MODEL - leave blank to raise a 404 error if the subdomain cannot be found, or add a url to redirect to instead.

## Bonus utils

You might find these useful for implementing a model subdomain system with your templates and views.

### Decorators

base_site_url is a decorator which requires a view to be called from the base site (i.e. with no subdomain). It redirects subdomained requests to the non subdomained equivalent. For example, http://foo.bar.com/eggs would be redirected to http://bar.com/eggs.

### Template tags

{% absurl view_name %} will return the full absolute url for the view. This absolute url is stripped of subdomains. Use exactly like {% url view_name %}

{% suburl view_name subdomain %} will return the full absolute url for the view with the subdomain as the first argument. Use exactly like {% url view_name %} but put the subdomain argument before any other view arguments. E.g. {% suburl article_detail author.user.username article.slug %} will create the url http://username.mysite.com/article-slug.

##TODO

Implement multiple models which can be matched in preference order.

