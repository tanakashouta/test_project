#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 17:11:31 2020

@author: tanakashouta
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]