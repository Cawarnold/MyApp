from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)


#urlpatterns = patterns('',
#    # Examples:
#    # url(r'^$', 'ecostuff.views.home', name='home'),
#    # url(r'^blog/', include('blog.urls')),
#
#    url(r'^admin/', include(admin.site.urls)),
#)
