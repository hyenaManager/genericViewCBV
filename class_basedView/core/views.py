from typing import Any, Dict
from django.shortcuts import get_object_or_404, render,HttpResponse
from django.views.generic import ListView,DetailView
from .models import Publisher,Book
import requests

class PublisherListView(ListView):
    model = Publisher
    context_object_name='my_favour_publisher'

class PublisherDetailView(DetailView):
    context_object_name = 'publisher_lists'
    queryset = Publisher.objects.all()

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context["book_list"] = Book.objects.all()
    #     return context
class BookList(ListView):
    context_object_name = 'book_lists'
    queryset = Book.objects.filter(publisher__name= "lime")
    template_name = "core/book_list.html"

class PublisherBookList(ListView):
    template_name = 'core/publisherBookList.html'
    context_object_name = 'publisher_books'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher,name = self.kwargs['publisher'])
        return Book.objects.get(publisher = self.publisher)
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["publisher"] = self.publisher
        return context
    
def api_check(request):

    url = "https://bloomberg-market-and-financial-news.p.rapidapi.com/market/auto-complete"

    querystring = {"query":"finacial"}

    headers = {
        "X-RapidAPI-Key": "cd59f31662mshca9f7cd43ea636ap1c82cdjsn91d94c188d4d",
        "X-RapidAPI-Host": "bloomberg-market-and-financial-news.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    context = data['news']
    print(context) 
    return render(request,'core/api_view.html',{"api_data":context})