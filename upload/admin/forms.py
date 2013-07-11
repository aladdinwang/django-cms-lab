from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _

class ZipUploadForm( forms.Form ):
    zipfile = forms.FileField( label = _('Zip Upload') )


