from django.shortcuts import render
from django.http import HttpResponse, Http404

#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime



def home(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = """<h1>Marion & Hugo </h1>
              <p>Vendredi 14 juillet 2017 à Nay</p>"""
    return HttpResponse(text)



def date_actuelle(request):

    return render(request, 'blog/date.html', {'date': datetime.now()})



