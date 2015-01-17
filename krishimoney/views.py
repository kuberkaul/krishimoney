from django.http import HttpResponse
from django.template import RequestContext

def adminForm(request, id):
    return HttpResponse("You're looking at question %s." % question_id)

def adminPageSubmitted(request):
    print "Hi" + str(request)
    return HttpResponse("You're looking at question")
