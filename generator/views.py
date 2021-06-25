from django.http.request import QueryDict
from django.http.response import HttpResponseBadRequest, HttpResponseBase
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
import random



def get_request_passgen(request):
    # return request.GET['length']
    buf_password = ''
    characters = list('abcdefghijklmopqrstuvwxyz')
    if 'uppercase' in request.GET:
        characters += list('ABCDEFGHIJKLMOPQRSTUVWXYZ')
    if 'numbers' in request.GET:
        characters += list('0123456789')
    if 'special_char' in request.GET:
        characters += list('!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~')
    random.shuffle(characters)
    for x in range(int(request.GET['length'])):
        buf_password += random.choice(characters)
    return buf_password

def post_request_passgen(request):
    return 'abracadabra_post'

def home(request):
    return render(request, 'generator/home.html')
    # return HttpResponseBadRequest('Hui tebe')

def password(request):
    buf_password = ''

    if request.method == 'GET':
        buf_password = get_request_passgen(request)
    elif request.method == 'POST':
        buf_password = post_request_passgen(request)
    
    # characters = list('abcdefghijklmopqrstuvwxyz')
    # length = 10
    # for x in range(length):
    #     buf_password += random.choice(characters)
    return render(request, 'generator/password.html', {'password':buf_password})

def about(request):
    return render(request, 'generator/about.html')