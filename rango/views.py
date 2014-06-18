from django.shortcuts import render

from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm


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

def add_category(request):
    # HTTP Post
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        
        # Is form valid?
        if form.is_valid():

            # Save category to database
            form.save(commit=True)

            # Call index and go to homepage
            return index(request)

        # If not valid form
        else:
            # Form errors (printed to terminal)
            print(form.errors)

    # HTTP Get
    elif request.method == 'GET':
        # Create form
        form = CategoryForm

    # Render form - include any error messages
    return render(request, 'rango/add_category.html', {'form': form})

    
def add_page(request, category_name_url):

    category_name = decode_url(category_name_url)
    
    if request.method == "POST":
        form = PageForm(request.POST)

        if form.is_valid():
            # Wait until all fields are populate before saving
            page = form.save(commit=False)

            # Is category in database?
            try:
                cat = Category.objects.get(name=category_name)
                page.category = cat
            # Category does note exist
            except:
                return render(request, 'rango/add_category.html',)

            # Add default value
            page.views = 0    

            # Save model instance when all fields are populated
            page.save()
           
            # Show the category page
            return category(request, category_name_url)
        else:
            print(form.errors)

    elif request.method == "GET":
        form = PageForm

    return render(request, 'rango/add_page.html', {
        'category_name_url': category_name_url,
        'category_name': category_name,
        'form': form,
    })

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
