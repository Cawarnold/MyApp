import datetime

from django.core.urlresolvers import reverse
from django.utils import timezone
from django.test import TestCase
from test_polls import *

from polls.models import Question, Choice


#### Notes on Tests ####

## 1. Test Django and models
## 2. Tests from the official guide, plus some extra that I wrote myself (20151211)
## 3. Tests from the pystar guide. -- These tests can be found in polls/test_polls.py


###########################################################################################################
###########################################################################################################
###########################################################################################################


######## 1. Test Django and models

#### Test version of django ####
import django
if django.VERSION < (1,7):
    raise Exception("Django version needs update")
else:
    print("Django correct version")

#### Test if models exist ####

models_importable = False
try:
    from polls.models import  Choice, Question
    models_importable = True
    print("Models imported fine")
except ImportError:
    pass


###########################################################################################################
###########################################################################################################
###########################################################################################################


######## 2. Tests from official guide

## Any function of a module (def of a class) that begins with test will be picked up in the running of the tests.
## The database is reset for each test method.

#### Test methods and functions ####

# Testing internal behavior of the code.

class QuestionMethodTests(TestCase):
    """
    This section is for testing the actual tables and functions
    """

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
    	"""
    	was_published_recently() should return False for questions whose
    	pub_date is older than 1 day.
    	"""
    	time = timezone.now() - datetime.timedelta(days=30)
    	old_question = Question(pub_date=time)
    	self.assertEqual(old_question.was_published_recently(), False)

	def test_was_published_recently_with_recent_question(self):
	    """
	    was_published_recently() should return True for questions whose
	    pub_date is within the last day.
	    """
	    time = timezone.now() - datetime.timedelta(hours=1)
	    recent_question = Question(pub_date=time)
	    self.assertEqual(recent_question.was_published_recently(), True)


#### Test a view ####

# Test behavior as it would be experienced by a user through a web browser


## A function that creates questions ##

def create_question(question_text, days):
    """
    Creates a question with the given `question_text` published the given
    number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text,
                                   pub_date=time)


## A function that creates choices ##

def create_choice(choice_text, question_id):
    """
    Creatas a choice with the given `choice_text` published for a given
    question that has been created using create_question.
    """
    return  Choice.objects.create(question = Question.objects.get(id=question_id), 
                                    choice_text = choice_text, 
                                    votes = 0)



class QuestionViewTests(TestCase):
    """
    Tests what is in the section of the site which has /polls/
    http://localhost:8000/polls/
    """
    def test_index_view_with_no_questions(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_a_past_question(self):
        """
        Questions with a pub_date in the past should be displayed on the
        index page.
        """
        question = create_question(question_text="Past question.", days=-30)
        question
        create_choice(choice_text="A Choice.", question_id=question.id)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_index_view_with_a_future_question(self):
        """
        Questions with a pub_date in the future should not be displayed on
        the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.",
                            status_code=200)
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        should be displayed.
        """
        question1 = create_question(question_text="Past question.", days=-30)
        question1
        question2 = create_question(question_text="Future question.", days=30)
        question2
        create_choice(choice_text="A Choice 1.", question_id=question1.id)
        create_choice(choice_text="A Choice 2.", question_id=question2.id)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_index_view_with_two_past_questions_ordered(self):
        """
        The questions index page may display multiple questions, 
        they will need to be displayed in order of pubishing date.
        """
        question1 = create_question(question_text="Past question 1.", days=-30)
        question1
        question2 = create_question(question_text="Past question 2.", days=-5)
        question2
        create_choice(choice_text="A Choice 1.", question_id=question1.id)
        create_choice(choice_text="A Choice 2.", question_id=question2.id)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )

    def test_index_view_with_6_questions_should_only_display_5(self):
        """
        The questions index page may display multiple questions, 
        they will need to be displayed in order of pubishing date.
        """
        question1 = create_question(question_text="Past question 1.", days=-1)
        question1
        question2 = create_question(question_text="Past question 2.", days=-2)
        question2
        question3 = create_question(question_text="Past question 3.", days=-3)
        question3
        question4 = create_question(question_text="Past question 4.", days=-4)
        question4
        question5 = create_question(question_text="Past question 5.", days=-5)
        question5
        question6 = create_question(question_text="Past question 6.", days=-6)
        question6
        create_choice(choice_text="A Choice 1.", question_id=question1.id)
        create_choice(choice_text="A Choice 2.", question_id=question2.id)
        create_choice(choice_text="A Choice 3.", question_id=question3.id)
        create_choice(choice_text="A Choice 4.", question_id=question4.id)
        create_choice(choice_text="A Choice 5.", question_id=question5.id)
        create_choice(choice_text="A Choice 6.", question_id=question6.id)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 1.>', '<Question: Past question 2.>', 
            '<Question: Past question 3.>', '<Question: Past question 4.>',
            '<Question: Past question 5.>']
        )

    def test_index_view_only_questions_with_choices(self):
        """
        If choices exist for specific question, then that question should be shown.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        question = create_question(question_text="A Question.", days=-5)
        question
        create_choice(choice_text="A Choice.", question_id=question.id)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: A Question.>']
        )

    def test_index_view_only_questions_with_NOchoices(self):
        """
        If no choices exist for specific question, then that question should not be shown.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        question1 = create_question(question_text="A Question 1.", days=-5)
        question1
        create_choice(choice_text="A Choice.", question_id=question1.id)
        question2 = create_question(question_text="A Question 2.", days=-5)
        question2
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: A Question 1.>']
        )


class QuestionIndexDetailTests(TestCase):
    """
    Tests what is in the section of the site which has /polls/1/
    http://localhost:8000/polls/1/
    """
    def test_detail_view_with_a_future_question(self):
        """
        The detail view of a question with a pub_date in the future should
        return a 404 not found.
        """
        future_question = create_question(question_text='Future question.',
                                          days=5)
        response = self.client.get(reverse('polls:detail',
                                   args=(future_question.id,)))
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_a_past_question(self):
        """
        The detail view of a question with a pub_date in the past should
        display the question's text.
        """
        past_question = create_question(question_text='Past Question.',
                                        days=-5)
        response = self.client.get(reverse('polls:detail',
                                   args=(past_question.id,)))
        self.assertContains(response, past_question.question_text,
                            status_code=200)


class QuestionIndexResultsTests(TestCase):
    """
    Tests what is in the section of the site which has /polls/1/results/
    http://localhost:8000/polls/1/results/
    """
    def test_results_view_with_a_future_question(self):
        """
        The results view of a question with a pub_date in the future should
        return a 404 not found.
        """
        future_question = create_question(question_text='Future question.',
                                          days=5)
        response = self.client.get(reverse('polls:results',
                                   args=(future_question.id,)))
        self.assertEqual(response.status_code, 404)

    def test_results_view_with_a_past_question(self):
        """
        The results view of a question with a pub_date in the past should
        display the question's text.
        """
        past_question = create_question(question_text='Past Question.',
                                        days=-5)
        response = self.client.get(reverse('polls:results',
                                   args=(past_question.id,)))
        self.assertContains(response, past_question.question_text,
                            status_code=200)

