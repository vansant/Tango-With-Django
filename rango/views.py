from django.http import HttpResponse

def index(request):
    about_link = '<a href="/rango/about">About</a>'
    return HttpResponse("Rango says: hello world!" + about_link)

def about(request):
    home_link = '<a href="/rango/">Home</a>'
    return HttpResponse("Rango says: here is the about page." + home_link)
