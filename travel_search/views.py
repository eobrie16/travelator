from django.shortcuts import render
from travel_search.models import Search
from travel_search.forms import SearchForm
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)



def index(request):
    return render(request, "index.html")

class AboutView(TemplateView):
    template_name = 'about.html'

class CreateSearchView(CreateView):
    redirect_field_name = 'search_detail'

    form_class = SearchForm
    model = Search

class SearchListView(ListView):
    model = Search

    # def get_queryset(self):
    #     return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class SearchDetailView(DetailView):
    model = Search

