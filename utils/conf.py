from django.conf import settings

def get_setting( key ):
    return getattr( settings, key )

def get_row_choices( prefix, limit ):
    choices = [( i, prefix + ' ' + str(i) ) for i in range( 1, limit ) ]
    return choices
