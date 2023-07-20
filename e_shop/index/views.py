from django.shortcuts import render
from . import forms

# Create your views here.
def home_page(request):
    search_bar = forms.SearchForm()
    context = {'form': search_bar}

    if request.method == 'POST':
        pass

    return render(request, 'index.html')


def about_page(request):
    return render(request, 'about.html')


def contact_page(request):
    return render(request, 'contacts.html')