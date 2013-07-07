# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, RequestContext
from demo.models import News
import requests
from django.template import Template
from django.utils.translation import ugettext_lazy as _

def publish( request ):
    if request.method == 'POST':
        title = request.POST['news_title']
        content = request.POST['news_content']
        author = request.POST['news_author']
        news = News( title = title, content = content,
                     author = author )
        news.save()
        context = Context( { 'news_title': title, 
                             'news_content': content,
                             'news_author': author }
                           )
    

        return render( request, 'news_print/publish_news.html', context )
    else:
        return render( request, 'news_print/publish_news.html', {} )

def allnews( request ):
    newslist = News.objects.all()[ : 5 ]
    context = Context( { 'newslist': newslist } )
    remote_url = "http://localhost:8000/templates/news/"
    r = requests.get( remote_url )
    print "-------------------print text-----------------"
    print r.text
    template = Template( r.text )
    
    return HttpResponse( template.render( context ) )
    


def show( request ):
    return RequestContext( request, {'news': News} )



def demo_photography(request):
    context = {'home': _("Photo Home"), 'feature': _("Photo Feature"), 
               'photography': _("Photo Photography"), 'service': _("Photo Service"), 
               'contact':_("Photo Contact"), 'store': _("Photo Store")}
    return render(request, 'demo_photography.html', context)
