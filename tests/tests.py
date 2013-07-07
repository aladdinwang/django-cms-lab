"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import os
from django.test import TestCase
from django.template.loader import get_template
from django.template import Template, Context
from django.conf import settings
#from django.shortcuts import render


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


def test_asy():
    t = get_template('generate_png.asy')
    image_path = settings.DEFAULT_IMAGE_PATH
    if not os.path.exists(image_path):
        os.makedirs(image_path)
    content = t.render(Context({'tips': 'haoba'}))
    from subprocess import Popen, PIPE
    print image_path
    p = Popen(['asy', '-o', image_path + '/world'], stdin=PIPE)
    p.wait()
    
