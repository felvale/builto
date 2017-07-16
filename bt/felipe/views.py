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
    return HttpResponse('felipe main page</br><a href="/main/">go back to main page</a>')
