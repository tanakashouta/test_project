#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 19:56:52 2020

@author: tanakashouta
"""

from django import forms

class HelloForm(forms.Form):
    name = forms.CharField(label='name')
    mail = forms.CharField(label='mail')
    age = forms.IntegerField(label='age')