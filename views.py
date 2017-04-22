from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import QuestionSession,Question
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.decorators import csrf
from core import decorators
from .forms import QuestionForm
def show_questioning_session(request, pk):
    question_session = get_object_or_404(QuestionSession, pk=pk)
    old_questions = question_session.question_set.all()
    old_questions = old_questions.order_by('-submission_date')
    last_pk = Question.objects.last().pk
    form = QuestionForm()
    return render(request, "question/index.html", {'question_session': question_session,
                                                   "last_pk": last_pk,
                                                   "old_question":old_questions,
                                                   'form': form})
@csrf.csrf_exempt
@decorators.ajax_only
def handle_questioning_ajax(request, pk):
    question_session = get_object_or_404(QuestionSession, pk=pk),
    old_last_pk = request.POST['last_pk']
    question_session_pk = request.POST['question_session_pk']
    new_last_pk = Question.objects.last().pk
    if old_last_pk != new_last_pk:
        new_questions = Question.objects.filter(id__gt=old_last_pk)
        new_questions = new_questions.values_list('question_text', flat=True)
        new_questions = list(new_questions)
        response= {'new_questions':new_questions,
                   'new_last_pk':new_last_pk}
    else:
        response={}
    return response
def add_question(request,pk):
    questionsession = get_object_or_404(QuestionSession, pk=pk)
    if request.method == "GET":
        form = QuestionForm()
    elif request.method == "POST":
        instance = Question(question_session = questionsession)
        form = QuestionForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('question:index', args=(pk,)))
    context = {
        'form':form
    }

    return render(request, 'question/index.html', context)