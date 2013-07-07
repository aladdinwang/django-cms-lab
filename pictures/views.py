# Create your views here.
from django.http import HttpResponse
from mimetypes import guess_type
from models import fs


def gridfs( request, fpath ):
    gs = fs.open( 'gridfs/' + fpath )
    return HttpResponse( gs.read(), mimetype = guess_type( fpath )[ 0 ] )
