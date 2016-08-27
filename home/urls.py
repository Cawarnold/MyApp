from django.conf.urls import patterns, url

from home import views

urlpatterns = patterns('',
	## url(regex, view, kwargs=None, name=None, prefix='')
    # ex: /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
)
