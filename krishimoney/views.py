from django.http import HttpResponse

def adminForm(request, id):
    return HttpResponse("You're looking at question %s." % question_id)

def adminPageSubmitted(id):
    print "Hi" + str(id)
    return HttpResponse(id)
