from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
  return render(request, 'index.html')

def random(request):
  if 'counter' in request.session:
    request.session['counter'] += 1
  else:
    request.session['counter'] = 1
  request.session['str_random']  = get_random_string(length=14)
      
  return redirect('/')

def reset(request):
  request.session.flush()
  return redirect('/')
