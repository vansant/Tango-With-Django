from django.shortcuts import render

def index(request):
    return render(request, 'rango/index.html', {'bold_message': 'This is the home page'})

def about(request):
    return render(request, 'rango/about.html', {'bold_message': 'This is the about page'})
