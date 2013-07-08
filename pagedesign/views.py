# Create your views here.
from django.http import HttpResponse
from django.contrib.formtools.wizard.views import SessionWizardView
from django import forms
from django.utils.translation import ugettext_lazy as _
from pagedesign.forms import MasterPageSelectForm, RowsInfoForm

class MasterPageSelectWizard( SessionWizardView ):
    picture_row_snippet_choices = (
        ( 'snippets/picture_2_column.html', _('Picture with 2 columns') ),
        ( 'snippets/picture_3_column.html', _('Picture with 3 columns') ),
        )
    def done( self, form_list, **kwargs ):
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
