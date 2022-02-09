from django.http import HttpResponse

def index (request):
    response = 'Hello there!'
    return HttpResponse(response)

def index2 (request):
    response = 'Hello from index 2!'
    return HttpResponse(response)