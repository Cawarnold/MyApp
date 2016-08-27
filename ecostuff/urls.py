from django.conf.urls import patterns, include, url
from django.contrib import admin

from ecostuff.home import views

urlpatterns = patterns('',
	url(r'^$', 'home.views.index')
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)


#urlpatterns = patterns('',
#    # Examples:
#    # url(r'^$', 'ecostuff.views.home', name='home'),
#    # url(r'^blog/', include('blog.urls')),
#
#    url(r'^admin/', include(admin.site.urls)),
#)
