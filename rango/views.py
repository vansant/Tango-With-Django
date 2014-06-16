from django.shortcuts import render
from rango.models import Category, Page


def encode_url(str):
    return str.replace(' ', '_')

def decode_url(str):
    return str.replace('_', ' ')

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
   
    for category in category_list:
        category.url = encode_url(category.name)
   
    return render(request, 'rango/index.html', {'categories': category_list, 'pages': page_list})

def about(request):
    return render(request, 'rango/about.html', {'bold_message': 'This is the about page'})

def category(request, category_name_url):
    # Replace spaces with an _ (underscore)
    category_name = decode_url(category_name_url)

    # Try to query category and the category's pages
    try:
        category = Category.objects.get(name=category_name)
        pages = Page.objects.filter(category=category)

    except Category.DoesNotExist:
        category = category_name
        pages = ""

    return render(request, 'rango/category.html', {"category": category, "pages": pages})
