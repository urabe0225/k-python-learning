#from django.http import Http404
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
#from django.template import loader
from django.urls import reverse_lazy
from django.utils import timezone

from .models import TodoModel

# ToDoの一覧表示

class TodoList(ListView):
    template_name = 'todo/list.html'
    model = TodoModel

# ToDoの詳細表示

class TodoDetail(DetailView):
    template_name = 'todo/detail.html'
    model = TodoModel

# ToDoの作成機能
class TodoCreate(CreateView):
    template_name = 'todo/create.html'
    model = TodoModel
    fields = ('title','contents','priority','duedate')
    success_url = reverse_lazy('list')

# ToDoの削除機能

class TodoDelete(DeleteView):
    template_name = 'todo/delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')

# ToDoの編集機能

class TodoUpdate(UpdateView):
    template_name = 'todo/update.html'
    model = TodoModel
    fields = ('title','contents','priority','duedate')
    success_url = reverse_lazy('list')

#class IndexView(generic.ListView):
#    template_name = "polls/index.html"
#    context_object_name = "latest_question_list"
#    
#    def get_queryset(self):
 #       """
  #      Return the last five published questions (not including those set to be
   #     published in the future).
    #    """
     #   return Question.objects.filter(duedate__lte=timezone.now()).order_by("-pub_date")[:5]
     
#    def get_queryset(self):
#        """Return the last five published questions."""
#        return Question.objects.order_by("-pub_date")[:5]


#class DetailView(generic.DetailView):
#    model = Question
#    template_name = "polls/detail.html"
#    def get_queryset(self):
#        """
#        Excludes any questions that aren't published yet.
#        """
#        return Question.objects.filter(duedate__lte=timezone.now())

#class ResultsView(generic.DetailView):
#    model = Question
 #   template_name = "polls/results.html"

#def index(request):
#    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    #template = loader.get_template("polls/index.html")
#    context = {"latest_question_list": latest_question_list}
#    return render(request, "polls/index.html", context)
    #return HttpResponse(template.render(context, request))
    #output = ", ".join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    #return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.

#def detail(request, question_id):
  #  question = get_object_or_404(Question, pk=question_id)
    #try:
        #question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
        #raise Http404("Question does not exist")
 #   return render(request, "polls/detail.html", {"question":question})
    #return HttpResponse("You're looking at the results of question %s." % question_id)

#def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, "polls/results.html", {"question": question})
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)

#def vote(request, question_id):
    #return HttpResponse("You're voting on question %s." % question_id)

#def vote(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    try:
#        selected_choice = question.choice_set.get(pk=request.POST["choice"])
#    except (KeyError, Choice.DoesNotExist):
#        # Redisplay the question voting form.
#        return render(
#            request,
#            "polls/detail.html",
##            {
  #              "question": question,
  #              "error_message": "You didn't select a choice.",
#            },
#        )
#    else:
#        selected_choice.votes += 1
#        selected_choice.save()

#        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))