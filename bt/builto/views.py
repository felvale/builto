"""
Builto app view module
"""
import logging

from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    """
    Function for main page rendering
    """
    return HttpResponse('main page for the hole site <br/> <a href="/chiara/"> go to chiara main page</a> <br/> <a href="/felipe/"> go to felipe main page</a>')
