from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth import authenticate,login,logout

from .models import Opcio, Consulta, Vot


class IndexView(generic.ListView):
    template_name = 'vota/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Consulta.objects.order_by('titul')[:5]

class DetailView(generic.DetailView):
    model = Consulta
    template_name = 'vota/detail.html'


class ResultsView(generic.DetailView):
    model = Consulta
    template_name = 'vota/results.html'

def vote(request, question_id):
    question = get_object_or_404(Consulta, pk=question_id)
    try:
        selected_choice = question.opcio_set.get(pk=request.POST['choice'])
    except (KeyError, Opcio.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'vota/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        vot = Vot()
        vot.opcio = selected_choice
        vot.usuari = request.user
        vot.save()


        #selected_choice.vots += 

        #selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('vota:results', args=(question.id,)))

def logearse(request):
    return render(request, 'vota/login.html')

def loginUser(request):
    user = request.POST['user']
    psswd = request.POST['password']
    logUser = authenticate(request, username=user, password=psswd)

    if logUser is not None:
        login(request,logUser)
        return HttpResponseRedirect('index',request)

    else:
        return render(request, 'vota/loginError.html',{
            'error_message': "You didn't login correct.",

            })
def logoutUser(request):
    if request.method == "POST":
        logout(request)
        
        return HttpResponseRedirect('home')