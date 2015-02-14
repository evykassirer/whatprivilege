from django.shortcuts import render_to_response
#from whatprivilege.models import Question

def home(request):
    #logics .... 
    return render_to_response('templates/home.html', {}) 

def instructions(request): 
    #logics....
    return render_to_response('templates/instructions.html',{})
