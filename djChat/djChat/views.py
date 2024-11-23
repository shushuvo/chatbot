from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .chat import reply

def homepage(request):
    return render(request, 'index.html')

@csrf_exempt
def handle_post(request):
    if request.method == 'POST':
        print("POST data received:", request.POST)
        message = request.POST.get('message')
        if message:
          return reply(message)
        else:
            return HttpResponse("Null error!")
    else:
        return HttpResponse("Status Code 405 Method Not allowed")