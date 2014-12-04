from django.conf.urls import patterns, include, url

from django.contrib import admin
from recommender import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WhereToGo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.select_activity, name='select_activity'),

    url(r'^admin/', include(admin.site.urls)),
)
