from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from .models import Item
from .forms import ItemForm



#item list view is implemented in salesmanager.urls.py file

class ItemListView(ListView):
    """List all the items"""
    model = Item
    template_name = 'salesmanager/item_list.html'
    context_object_name = 'items'

class ItemCreateView(CreateView):
    """Create view for item model"""
    model = Item
    template_name = 'salesmanager/item_create_form.html'
    fields = ('name','tag', 'category', 'company', 'price',)
    success_url = '/'

class ItemDetailView(DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'salesmanager/item_detail.html'
#
# def create_item(request):
#     """function to create item"""
#
#     form = {}
#     if request.method == "POST":
#         form['item_form'] = ItemForm(request.POST)
#
#         if form['item_form'].is_valid():
#             item = form['item_form'].save(commit=False)
#             item.updated_at = timezone.now()
#             item.save()
#             return HttpResponseRedirect("/")
#
#     else:
#         form['item_form'] = ItemForm()
#
#     return render(request, 'salesmanager/item_create_form.html', form)
#




def dashboard(request):
    """Just render the dashboard page"""
    return render(request, 'salesmanager/base.html', {})
