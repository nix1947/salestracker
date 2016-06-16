from django.conf.urls import url, include
from .views import CompanyListView, CompanyCreateView, CompanyUpdateView, \
CompanyDeleteView, CompanyDetailView


urlpatterns = [
    url(r'^$',CompanyListView.as_view(), name="companies"),
    url(r'company/(?P<pk>\d+)/$', CompanyDetailView.as_view(), name="company"),
    url(r'add/$', CompanyCreateView.as_view(),name="add"),
    url(r'update/(?P<pk>\d+)/$', CompanyUpdateView.as_view(), name="update"),
    url(r'delete/(?P<pk>\d+)/$', CompanyDeleteView.as_view(), name="delete"),

]
