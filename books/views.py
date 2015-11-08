from django.shortcuts import render,render_to_response
from django.http import Http404,HttpResponse,HttpResponseRedirect
from models import Book
from forms import ContactForm

# Create your views here.

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',{'books': books,'query': q})
    return render_to_response('search_form.html',{'errors': errors})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return HttpResponseRedirect('/books/thanks/')
    else:
        form = ContactForm(initial={'subject': 'I love your site!'})
    return render_to_response('contact_form.html',{'form': form})

def thanks(request):
    return render_to_response('thanks.html')
