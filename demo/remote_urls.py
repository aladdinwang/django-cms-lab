from django.conf import settings
from django.template.loader import BaseLoader
import requests


class Loader( BaseLoader ):
    def load_template( self, remote_url, template_dirs = None ):
        r = requests.get( remote_url )
        template = Template( r.text )
        return template, remote_url
        
