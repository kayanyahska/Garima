# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from utilities import plotMap


# Create your views here.

def index(request):

	return render(request, 'alpha3.html', {})

def showMap(request):
		a = request.GET['apoint']
		b = request.GET['bpoint']

		print(a)
		print(b)

		mp = plotMap.findPath(a, b)

		return render(request, 'map.html', {})