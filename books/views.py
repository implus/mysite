# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from books.models import Book
from books.models import Publisher
from django.views.generic import ListView
from django.utils import timezone

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET.get('q')
        if not q:
            errors.append('Enter a search term')
        elif len(q) > 20:
            errors.append('Please input at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',{'books': books, 'query': q})
    #else:
        #return HttpResponse('Please submit a search term.')
    return render_to_response('search_form.html',{'errors': errors})

class PublisherListView(ListView):
    model = Publisher
    def get_context_data(self, **kwargs):
        context = super(PublisherListView,self).get_context_data(**kwargs)
        #context['template_name']= 'templates/publisher_list.html'
        context['now'] = timezone.now()
        return context