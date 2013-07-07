import ConfigParser
from django.conf import settings
from django.template.loader import BaseLoader


class FakeTemplate:
    def __init__( self, http_content ):
        self.http_content = http_content
        
    def render( self, context ):

class Loader( BaseLoader ):
    is_usable = True
    
    def load_template
