# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context
from django import forms
from Account.models import User
from django.contrib.auth.hashers import make_password, check_password

class UserForm( forms.Form ):
    user_name = forms.CharField( max_length=100 )
    passwd = forms.CharField( max_length = 50 )


def register( request ):
    if request.method == 'POST':
        user_name = request.POST[ "user_name" ]
        passwd = request.POST[ "passwd" ]
        passwd2 = request.POST["passwd2"]
        
        msg = ""
        def error_msg():
            return msg
        context2 = Context( { 'user_name': user_name, 'passwd': passwd, 'msg': error_msg() } )
        if passwd != passwd2:
            context = Context( { 'user_name': user_name, 'passwd': passwd, 'msg': "Password isn't consistent!" } )
            #msg = "Password isn't consistent!"
            return render( request, 'register.html', context )
        
        if -1 != user_name.find( " " ) or -1 != passwd.find( " " ):
            context = Context( { 'user_name': user_name, 'passwd': passwd, 'msg': "Illegal input!" } )
            return render( request, 'register.html', context )

        if len( User.objects.filter( name = user_name ) ):
            context = Context( { 'user_name': user_name, 'passwd': passwd, 'msg': "Already has user: " + user_name } )
            return render( request, 'register.html', context )        

        passwd = make_password( passwd, hasher="md5" )        
        user = User( name = user_name, passwd = passwd )
        user.save()
        request.session["logged_on"] = True
        
        return render( request, "working.html", {} )
            
    else:
        context = {}
            
    return render( request, 'register.html', \
                       context )



            
def login( request ):
    if request.method == 'POST':
        user_name = request.POST[ "user_name" ]
        passwd = request.POST[ "passwd" ]
                
        user = User( name = user_name )
        user = User.objects.filter( name = user_name )
        
        
        
        if 0 == len( user ):
            context = Context( { 'user_name': user_name, 'passwd': passwd, 'msg': "User doesn't exist!" } )
            return render( request, 'login.html', context )
        
        user = user[0]
        
        if not check_password( password = passwd, encoded = user.passwd, preferred = "md5" ):
            msg = "Password is not correct!"
            context = Context( { 'user_name': user_name, 'passwd': passwd, 'msg': "Password is not correct!" } )
            return render( request, 'login.html', context )
        
        return render( request, "working.html", {} )
            
    else:
        context = {}
            
    return render( request, 'login.html', \
                       context )
    


def work( request ):
    if request.method == "POST":
        request.session.clear()
        return render( request, "register.html", {} )

    if request.session.get( "logged_on", False ):
        return render( request, 'working.html', {} )

    else:
        return HttpResponse( "You haven't logged in!" )
