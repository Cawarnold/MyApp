from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic

from django.utils import timezone

from polls.models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last 5 published questions (not including those set to be
        published in the future).
        """
        #return Question.objects.filter(
        #    pub_date__lte=timezone.now()
        #).order_by('-pub_date')[:5]

        return [i for i in Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5] if i.choice_set.exists()]

# template name tells the IndexView to use our existing "polls/index.html" template.
# Similarily for DetailView. ## Its called "Subclassing generic views"
