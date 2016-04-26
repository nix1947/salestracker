from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy


from .models import Item
from .forms import ItemForm

#company class import
from .models import Company
from .forms import CompanyForm



#item list view is implemented in salesmanager.urls.py file

class ItemListView(ListView):
    """List all the items"""
    model = Item
    template_name = 'salesmanager/item_list.html'
    context_object_name = 'items'

class ItemCreateView(CreateView):
    """Create view for item model"""
    model = Item
    form_class = ItemForm
    template_name = 'salesmanager/item_create_form.html'
    # fields = ('name','tag', 'category', 'company', 'price',)
    success_url = reverse_lazy("items:items")

class ItemDetailView(DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'salesmanager/item_detail.html'


class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'salesmanager/item_form.html'

class ItemDeleteView(DeleteView):
    model = Item
    success_url = reverse_lazy('items:items')


#Company models related views##

class CompanyCreateView(CreateView):
    """Creating company model"""
    model = Company
    template_name = 'salesmanager/company_create_form.html'
    form_class = CompanyForm
    success_url = reverse_lazy("companies:companies")



class CompanyListView(ListView):
    model = Company
    template_name = 'salesmanager/company_list.html'
    context_object_name = 'companies'


class CompanyUpdateView(UpdateView):
    model = Company
    template_name = 'salesmanager/company_form.html'
    context_object_name = 'company'
    form_class = CompanyForm


class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'salesmanager/company_confirm_delete.html'
    success_url = reverse_lazy("companies:companies")

    # don't need to define fields when define form_class
    # fields = ('name','tag', 'category', 'company', 'price',)
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
