from django.conf.urls import url
from .models import Item
from .views import ItemListView, ItemDetailView

from . import views


app_name = 'items'

urlpatterns = [
    #url that serve the listing of items

    #list of items
    url(r'^$',ItemListView.as_view(), name="items"),
    #single item detail
    url(r'item/(?P<pk>\d+)/$',ItemDetailView.as_view(),name="item"),
    #url to edit the items
    url(r'create/$', views.ItemCreateView.as_view(), name="create_item"),
]
