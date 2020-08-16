from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm
from .models import Friend

# Create your views here.
def index(repuest):
    params = {
        'title' : 'Hello/Index',
        'message' : 'all friends.',
        'form' : HelloForm(),
        'data' : [],
    }
    if (repuest.method == 'POST'):
        num = repuest.POST['id']
        item = Friend.objects.get(id=num)
        params['data'] = [item]
        params['from'] = HelloForm(repuest.POST)
    else:
        params['data'] = Friend.objects.all()
    return render(repuest, 'hello/index.html', params)    
