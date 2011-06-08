#django-model-subdomains

This middleware allow models to have subdomains, to create for example username.yoursite.com style websites.

First other subdomains are checked (e.g. blog.yoursite.com, api.yoursite.com) before model objects are.

If a subdomain is matched, the url conf associated with that subdomain is used for all requests, the subdomains is added to the request object (request.subdomain) and if a model is matched, the object is added to the request object for use in views (request.subdomain_object).

## Installation

1. Copy subdomain_middleware.py and subdomain_settings.py into your project.
2. Add 'subdomain_middleware.SubdomainMiddleware' to your MIDDLEWARE_CLASSES in your project settings.py file.
3. Set up the subdomain_settings.py file - set up the model you want to subdomain, as well as the url_confs for the model subdomains and other subdomains.
4. Create the url confs needed for the subdomains. 

## Example Configuration

An example configuration is included with model_urls.py being the url conf used if a model is matched on a subdomain, otherwise the default urls.py is used. 

## Settings

MODEL_TO_SUBDOMAIN takes two fields, 'model' and 'filter_field' which should take the model type and the name of the field to filter using the subdomain to find the associated model.

MODEL_SUBDOMAIN_URLCONF is the url conf to use if a model is found.

SUBDOMAIN_URLCONFS takes subdomain names and the associated url conf to use if a match is found. These subdomains are matched prior to any models (so make sure noone has a username 'blog' for example).

REDIRECT_IF_NO_MODEL - leave blank to raise a 404 error if the subdomain cannot be found, or add a url to redirect to instead.

##TODO

Implement multiple models which can be matched in preference order.

