from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Question, Training


def index(request):
    latest_trainings_list = Training.objects.order_by('-date')[:5]
    template = loader.get_template('polls/trainings.html')
    context = {
        'latest_trainings_list': latest_trainings_list,
    }
    return HttpResponse(template.render(context, request))


def training_details(request, training_id):
    training = get_object_or_404(Training, pk=training_id)
    return render(request, 'polls/training.html', {'training': training})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)