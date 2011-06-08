"""
This is the settings file for the subdomains.
Below the fields are filled in with an example implementation
"""

#the model to subdomain and the key to search on
from MyApp.models import MyModel
MODEL_TO_SUBDOMAIN = {
    'model' : MyModel,
    'filter_field' : 'slug', #will catch foo.mysite.com if foo can be matched to a slug of MyModel
}

#the url conf if a model is matched
MODEL_SUBDOMAIN_URLCONF = 'model_urls'

#these subdomains are checked before models
SUBDOMAIN_URLCONFS = {
    'blog' : 'blog_urls', #will catch blog.mysite.com
    'api' : 'api_urls',
}

#leave blank if you want to 404 instead
REDIRECT_IF_NO_MODEL = 'http://mysite.com'

