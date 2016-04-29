from django.conf.urls import url
from .models import Item
from .views import ItemListView, ItemDetailView, ItemDeleteView

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

    #update an item
    url(r'update/(?P<pk>\d+)/$', views.ItemUpdateView.as_view(), name="update_item"),

    #delete an item
    url(r'delete/(?P<pk>\d+)/$', views.ItemDeleteView.as_view(), name="delete_item"),

    #url to list the all sold items
    url(r'sold/$',views.ListSoldItem.as_view(), name='sold_items'),

    #url to list the all new items
    url(r'new/$', views.ListNewItem.as_view(), name="new_items")
]
