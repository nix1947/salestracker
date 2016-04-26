from django.conf.urls import include, url
from django.contrib import admin
from salesmanager.views import dashboard

urlpatterns = [
    # Examples:
    # url(r'^$', 'salestracker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url for product items
    url(r'items/', include('salesmanager.urls', namespace="items")),
    #for company
    url(r'^companies/', include('salesmanager.company_urls',namespace="companies")),
    #for dashboard
    url(r'dashboard/$',dashboard, name="dashboard"),

    url(r'^admin/', include(admin.site.urls)),
]
