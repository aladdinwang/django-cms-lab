from django import forms
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from cms.utils.conf import get_cms_setting
from utils.conf import get_row_choices

class MasterPageSelectForm( forms.Form ):
    masterpages = ( ( _("Index Page"), "index.html" ),
                    ( _("Account Page"), "account.html" ), )
    base_templates = get_cms_setting( 'BASE_TEMPLATES' )
    base_template_prefix = get_cms_setting( 'BASE_TEMPLATE_PREFIX' )
    base_templates = [ ( base_template_prefix + p, t ) for ( p, t ) in base_templates ]

    row_choices = get_row_choices( _( "Row" ), 8 )
    print row_choices
    base_templates = forms.ChoiceField( choices = base_templates, label = _("masterpage"), 
                                    required = False, help_text = _( "This is the master page type" ) )
    rows = forms.ChoiceField( choices = row_choices, required = False, label = _("Row"), 
                              help_text = _("How many rows?") )


class RowsInfoForm( forms.Form ):
    pass



