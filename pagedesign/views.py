# Create your views here.
from django.http import HttpResponse
from django.contrib.formtools.wizard.views import SessionWizardView
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.template.loader import get_template, render_to_string
from django.utils.safestring import mark_safe
from django.template import Context
from pagedesign.forms import MasterPageSelectForm, RowsInfoForm

class MasterPageSelectWizard( SessionWizardView ):
    picture_row_snippet_choices = (
        ( 2, _('Picture with 2 columns') ),
        ( 3, _('Picture with 3 columns') ),
        )
    base_template_name = "base/photography.html"
    def done( self, form_list, **kwargs ):
        placeholder_template = " placeholder %(placeholder_name)s group=image tips=%(placeholder_tips)s " \
            "width=216 height=168 "
        cleaned_data = self.get_all_cleaned_data()
        #print cleaned_data
        row_count = int( cleaned_data.get( 'rows', 0 ) )
        picture_rows = []
        picture_id = 1

        for row in range( 1, row_count + 1 ):
            key = 'row' + str( row )
            # may use get
            picture_cols = []
            col_count = int( cleaned_data[ key ] )
            for col in range( 0, col_count  ):
                picture = {}
                substitution = {
                    'placeholder_name':  "photo%s" % str( picture_id ),
                    'placeholder_tips':  "Design for photo%s" % ( str( picture_id ) ),
                }
                picture_id += 1
                picture[ 'placeholder' ] = placeholder_template % substitution
                picture[ 'url' ] = '#'
                picture[ 'name' ] = substitution[ 'placeholder_name' ]
                picture_cols.append( picture )
                
            picture_rows.append( picture_cols )
        
        
        template = render_to_string( self.base_template_name, Context( { 'picture_rows': picture_rows } ) )
        print mark_safe( template )
        return HttpResponse( "OK"  )
    def get_form( self, step = None, data = None, files = None ):
        if '1' == step:
            raw_data = self.storage.get_step_data( '0' )
            count = raw_data.get( '0-rows', 0 )
            count = int(count)
            
            if not count:
                form.fields['wrongfield'] = forms.CharField( label = 'Something wrong' )
            else:
                form_class = RowsInfoForm
                form_class.base_fields.clear()
                for i in range( 1, count + 1 ):
                    name = 'row' + str( i )
                    label = 'Row ' + str( i )
                    form_class.base_fields[name] = forms.ChoiceField( label = label, choices = MasterPageSelectWizard.picture_row_snippet_choices )
                self.form_list['1'] = form_class

        form = super( MasterPageSelectWizard, self ).get_form( step, data, files )
        return form
