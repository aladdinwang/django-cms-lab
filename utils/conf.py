from django.conf import settings
from configobj import ConfigObj
import os

CMS_TEMPLATE_DEFAULTS = [
    ('template_1.html', 'Template One'),
    ('template_2.html', 'Template Two'),
    ( 'news_template.html', 'News Template' ),
    ( 'imageurl.html', 'Image Url' ),
    ('photography.html', 'Photography'),
]


def get_setting( key ):
    return getattr( settings, key )

def get_row_choices( prefix, limit ):
    choices = [( i, prefix + ' ' + str(i) ) for i in range( 1, limit ) ]
    return choices

def init_extend_cfg( filename = settings.EXTEND_CONFIG_FILE ):
    config = ConfigObj( filename )
    config['CMS_TEMPLATE_DEFAULTS'] = CMS_TEMPLATE_DEFAULTS
    config.write()
    return 


def get_extend_cfg( filename = settings.EXTEND_CONFIG_FILE ):
    config = ConfigObj( filename )
    return config


def update_tuple_list( tuple_list, first, second ):
    i = 0
    for ( k, v ) in tuple_list:
        if k == first:
            tuple_list[i] = ( first, second )
            return
        i += 1
    tuple_list.append( ( first, second ) )
