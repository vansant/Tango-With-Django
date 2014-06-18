from django import forms
from rango.models import Page, Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    # Inline class to provide additional information on the form
    class Meta:
        # Associate ModelForm to model Category
        model = Category

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL or the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)


    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url:
            # Prepend http:// if no protocol is specified
            if not url.startswith('http://'):
                url = "http://" + url
                cleaned_data['url'] = url
        return cleaned_data

    class Meta:
        # Associate ModelForm to model Page
        model = Page

        # Choose fields (columns) to include with form
        # Not all fields in model are always required and may allow NULL values
        # In this case, we are hiding the foreign key
        fields = ('title', 'url', 'views')
