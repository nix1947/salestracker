from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'salestracker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^dashboard/$', 'salesmanager.views.dashboard'),
    url(r'^admin/', include(admin.site.urls)),
]
