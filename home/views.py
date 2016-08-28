from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic

from django.utils import timezone

from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = 'home/index.html'