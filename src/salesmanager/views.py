import string, random

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
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
    template_name = 'salesmanager/item/item_list.html'
    context_object_name = 'items'
    paginate_by = 20

class ItemCreateView(CreateView):
    """Create view for item model"""
    model = Item
    form_class = ItemForm
    template_name = 'salesmanager/item/item_create_form.html'
    # fields = ('name','tag', 'category', 'company', 'price',)
    success_url = reverse_lazy("items:items")

    def get_initial(self):
        """Pre populate the data field"""

        size = 6 #generate random tag of length 6
        chars=string.ascii_uppercase + string.digits
        random_tag =  ''.join(random.choice(chars) for _ in range(size))
        initial = super(ItemCreateView, self).get_initial()
        initial["tag"] = random_tag
        return initial

class ItemDetailView(DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'salesmanager/item/item_detail.html'


class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'salesmanager/item/item_form.html'

class ItemDeleteView(DeleteView):
    model = Item
    success_url = reverse_lazy('items:items')
    template_name = 'salesmanager/item/item_confirm_delete.html'

class ListSoldItem(ListView):
    queryset = Item.objects.filter(status='sold')
    template_name = 'salesmanager/item/item_list.html'
    context_object_name = 'items'
    paginate_by = 20


def list_new_item(request):
    objects_list = Item.objects.filter(status='new')
    paginator = Paginator(objects_list, 20) #20 items per page
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except EmptyPage:
        #deliver last page
        items = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        items = paginator.page(1) #deliver first page if page query is not integer

    return render(request, 'salesmanager/item/item_list.html', {'items':items, 'page':items})


class ListNewItem(ListView):
    queryset = Item.objects.filter(status='new')
    paginate_by = 20
    template_name = 'salesmanager/item/item_list.html'
    context_object_name = 'items'

#Company models related views##

class CompanyCreateView(CreateView):
    """Creating company model"""
    model = Company
    template_name = 'salesmanager/company/company_create_form.html'
    form_class = CompanyForm
    success_url = reverse_lazy("companies:companies")



class CompanyListView(ListView):
    model = Company
    template_name = 'salesmanager/company/company_list.html'
    paginate_by=20
    context_object_name = 'companies'


class CompanyUpdateView(UpdateView):
    model = Company
    template_name = 'salesmanager/company/company_form.html'
    context_object_name = 'company'
    form_class = CompanyForm


class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'salesmanager/company/company_confirm_delete.html'
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
