from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
def home(request):
    print("parâmetro request:",request)
    return HttpResponse("<h1>Página Home</h1>")
